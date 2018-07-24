using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;

namespace RazorFun.Controllers
{



    public class indexController : Controller
    {
        
        [HttpGet]
        [Route("")]
        public IActionResult index()
        {
            
            
            return View("index");
        }
    }
}