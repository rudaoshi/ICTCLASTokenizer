#include <boost/python.hpp>

#include "Result.h"
#include <string>

using namespace std;

class ICTCLASSegmenterCore
{
	CResult * result;
	char * output_buff;
	
public: 
	ICTCLASSegmenterCore(const string & data_dir_path)
	{
		result = new CResult(data_dir_path.c_str());
		output_buff = new char[1024*100];
	}
	
	~ICTCLASSegmenterCore()
	{
		delete result;
		delete[] output_buff;
	}
	
	string Segment(const string & paragraph)
	{

		bool ret = result->ParagraphProcessing((char*)paragraph.c_str(), output_buff);
    	if (ret)
    	{
    		string result_str(output_buff);
    		return result_str;
   		}
    	else
    	{
        	throw runtime_error("Error in segmentation ");
    	}
	}
};


BOOST_PYTHON_MODULE(libpyICTCLASCore)
{
    using namespace boost::python;
    class_<ICTCLASSegmenterCore>("ICTCLASSegmenterCore", init<const std::string &>())
        .def("Segment", &ICTCLASSegmenterCore::Segment);
}