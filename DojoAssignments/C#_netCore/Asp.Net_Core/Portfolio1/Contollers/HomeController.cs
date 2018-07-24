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
            return View("Index");
        }
        [HttpGet]
        [Route("projects")]
        public string Index2()
        {
            return "These are my projects";
        }
        [HttpGet]
        [Route("contact")]
        public string Index3()
        {
            return "This is my Contact!";
        }


    }
}