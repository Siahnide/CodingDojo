using System.ComponentModel.DataAnnotations;
using Microsoft.EntityFrameworkCore;
namespace test.Models
{
    public class Sakila
    {
        public class SakilaContext : DbContext
        {
            public SakilaContext(DbContextOptions options) : base(options) {}
        }
    }
}