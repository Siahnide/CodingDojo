using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;


namespace Portfolio2.Controllers
{



    public class HomeController : Controller
    {
        
        [HttpGet]
        [Route("")]
        public IActionResult home()
        {
            return View();
        }
        [HttpGet]
        [Route("projects")]
        public IActionResult projects()
        {
            return View();
        }
        [HttpGet]
        [Route("contact")]
        public IActionResult contact()
        {
            return View();
        }


    }
}