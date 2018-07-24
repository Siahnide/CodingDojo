using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;


namespace Portfolio1.Controllers
{



    public class HomeController : Controller
    {
        
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            int? gold = HttpContext.Session.GetInt32("Gold");
            if(gold == null)
            {
                HttpContext.Session.SetInt32("Gold",0);
                gold = 0;
            }
            ViewBag.Gold = gold;
            return View("Index");
            
        }

        [HttpPost]
        [Route("gold")]
        public IActionResult golding(string building)
        {
            if(building == "cavern")
            {
                
            }
            if(building == "lair")
            {

            }
            if(building == "nana")
            {

            }
            if(building == "castle")
            {

            }

            return RedirectToAction("Index") ;
        }

    }
}