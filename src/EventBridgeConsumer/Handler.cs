using System;
using System.Web;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;
using Amazon.Lambda.Core;
using Amazon.Lambda.CloudWatchEvents;
using System.Text;
using Newtonsoft.Json;

[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.Json.JsonSerializer))]
namespace EventBridgeConsumer
{
    public class Handler
    {
        public Handler()
        {

        }

        public async Task<bool> FunctionHandler(CloudWatchEvent<object> input, ILambdaContext context)
        {
            System.Console.WriteLine("Hello from EventBridge");
            var payloadModel = JsonConvert.SerializeObject(input);
            Console.WriteLine($"{payloadModel}");
            return true;
        }
    }

}
