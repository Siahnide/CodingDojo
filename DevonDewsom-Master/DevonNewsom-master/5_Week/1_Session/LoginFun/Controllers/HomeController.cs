using System.Collections.Generic;
using System.Linq;
using LoginFun.Models;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;

namespace LoginFun.Controllers
{
    
    public class HomeController : Controller
    {

       
        [HttpGet("")]
        public IActionResult Index()
        {
            // string Name = "Josiah";
            // List<Dictionary<string, object>> users = DbConnector.Query($"SELECT * FROM users WHERE username = '{Name}'");
            // ViewBag.Users = users;
            return View();
        }
       [HttpPost("Registration")]
       public IActionResult Registration(RegistrationUser user)
       {

        
            if(ModelState.IsValid)
            {
                // Create Our User (BUT HASH THE PW)
                PasswordHasher<RegistrationUser> hasher = new PasswordHasher<RegistrationUser>();
                string hash = hasher.HashPassword(user, user.password);

                string SQL = $"INSERT INTO users (username,email,password) VALUES ('{user.first_name}','{user.email}',{hash}')";
                DbConnector.Execute(SQL);
                // now what?
                TempData["message"] = "You may now login!";
                return View("Login");
            }
            else
            {
            return View("Failure");

            }

           
       }
        [HttpPost("Login")]
        public IActionResult Login(LoginUser user)
        {
            List<Dictionary<string, object>> result = DbConnector.Query($"SELECT * FROM users WHERE email = '{user.email}'");
            // check existance of user with user.email
            if(result.Count < 1)
            {
                // ERROR
                ModelState.AddModelError("email", "Invalid Email/Password");
            }
            else
            {
                string hashedPWFromDB = (string)result[0]["password"];
                // compare hashed pw in db against user's plaintext pw attempt
                PasswordHasher<LoginUser> hasher = new PasswordHasher<LoginUser>();

                PasswordVerificationResult TestResultFailed = PasswordVerificationResult.Failed;
                PasswordVerificationResult TestResultSuccess = PasswordVerificationResult.Success;

                PasswordVerificationResult PW_ATTEMPT_RESULT = hasher.VerifyHashedPassword(user, hashedPWFromDB, user.password);
                if(PW_ATTEMPT_RESULT == PasswordVerificationResult.Failed)
                {
                    // ERROR
                    ModelState.AddModelError("email", "Invalid Email/Password");
                }
                return Json("SUCCESS");
            }


            return RedirectToAction("Index");
        }
    }
}