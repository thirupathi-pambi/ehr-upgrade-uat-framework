import csv,json
from collections import Counter,defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
VALID={'pass','fail','blocked','not_run'}

def summarize(rows):
    rows=list(rows)
    if any(r['status'] not in VALID for r in rows):raise ValueError('Invalid test status')
    totals=Counter(r['status'] for r in rows)
    modules=defaultdict(Counter)
    for r in rows:modules[r['module']][r['status']]+=1
    return {'total':len(rows),'pass_rate_pct':round(100*totals['pass']/len(rows),1) if rows else 0,
            'open_defects':sorted({r['defect_id'] for r in rows if r['status'] in ('fail','blocked') and r['defect_id']}),
            'release_gate':'REVIEW REQUIRED' if totals['fail'] or totals['blocked'] or totals['not_run'] else 'READY FOR REVIEW',
            'by_module':{k:dict(v) for k,v in sorted(modules.items())}}

def main():
    with (ROOT/'data/test_cases.csv').open() as f:result=summarize(csv.DictReader(f))
    out=ROOT/'output/uat_summary.json';out.parent.mkdir(exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
