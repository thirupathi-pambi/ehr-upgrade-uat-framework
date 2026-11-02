import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from main import summarize
class UATTests(unittest.TestCase):
 def test_release_gate(self):self.assertEqual(summarize([{'module':'x','status':'fail','defect_id':'D1'}])['release_gate'],'REVIEW REQUIRED')
 def test_all_pass(self):self.assertEqual(summarize([{'module':'x','status':'pass','defect_id':''}])['pass_rate_pct'],100)
