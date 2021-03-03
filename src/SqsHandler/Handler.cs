using System;
using System.Web;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;
using Amazon.Lambda.Core;
using Amazon.Lambda.SQSEvents;

[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.Json.JsonSerializer))]
namespace SqsHandler
{
    public class Handler
    {
        public Handler()
        {

        }

        public async Task<bool> FunctionHandler(SQSEvent sqsEvent, ILambdaContext context)
        {
            if (sqsEvent.Records.Count == 0)
            {
                Console.WriteLine("No records found.");
                return false;
            }
            foreach (var record in sqsEvent.Records)
            {
                System.Console.WriteLine("Hello from the SQS handler");
                System.Console.WriteLine(record.Body);
            }
            return true;
        }
    }

}
