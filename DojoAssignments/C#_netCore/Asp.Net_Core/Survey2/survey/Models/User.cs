using System.ComponentModel.DataAnnotations;

namespace survey.Models

{
    public class User
    {
        [Required]
        [MinLength(4)]
        public string FirstName {get;set;}
        [Required]
        [MinLength(4)]
        public string LastName {get;set;}
        [Required]
        [Range(1,110)]
        public string Age {get;set;}
        [Required]
        [EmailAddress]
        public string Email {get;set;}
        [Required]
        [MinLength(8)]
        public string Password {get;set;}

    }
}
