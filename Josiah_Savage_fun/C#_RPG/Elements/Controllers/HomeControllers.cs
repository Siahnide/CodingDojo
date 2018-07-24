using Microsoft.AspNetCore.Mvc;
namespace TimeDisplay.Controllers
{
    public class homeController : Controller
    {
        [HttpGet]
        [Route("")]
        public IActionResult Level_1()
        {
            return View();
        }
    }
}