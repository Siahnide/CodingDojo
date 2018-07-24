namespace Models.User
{
    public class RegistrationUser
    {   
        [Required]
        public string username {get;set;}
        [Required]
        public string password {get;set;}
        [Required]
        public string email {get;set;}
        
    }
}
