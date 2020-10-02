# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 15:37:10 2020

@author: harinder
"""
import yaml

def convert_to_jmx():
    filename = "result/jmeter.jmx"
    
    stream = open("result/jmeter.yml","r")
    my_dicts = yaml.load_all(stream)
    
    with open(filename,"w") as xmlfile:
        for my_dict in my_dicts:
            for k,v in sorted(my_dict.items()):
                if k=="Name":
                    testplanName="<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n\
                    <jmeterTestPlan version=\"1.2\" properties=\"5.0\" jmeter=\"5.3\">\n\
                      <hashTree>\n\
                        <TestPlan guiclass=\"TestPlanGui\" testclass=\"TestPlan\" testname=\""+ str(v) +"\" enabled=\"true\">\n\
                          <stringProp name=\"TestPlan.comments\"></stringProp>\n\
                          <boolProp name=\"TestPlan.functional_mode\">false</boolProp>\n\
                          <boolProp name=\"TestPlan.tearDown_on_shutdown\">true</boolProp>\n\
                          <boolProp name=\"TestPlan.serialize_threadgroups\">false</boolProp>\n\
                          <elementProp name=\"TestPlan.user_defined_variables\" elementType=\"Arguments\" guiclass=\"ArgumentsPanel\" testclass=\"Arguments\" testname=\"User Defined Variables\" enabled=\"true\">\n\
                            <collectionProp name=\"Arguments.arguments\"/>\n\
                          </elementProp>\n\
                          <stringProp name=\"TestPlan.user_define_classpath\"></stringProp>\n\
                        </TestPlan>\n\
                        <hashTree>\n\
                        <ThreadGroup guiclass=\"ThreadGroupGui\" testclass=\"ThreadGroup\" testname=\""+ str(v) +"\" enabled=\"true\">\n"
                    xmlfile.write(str(testplanName))
                if k=="TestConcurrency":
                    concurrency="<stringProp name=\"ThreadGroup.on_sample_error\">continue</stringProp>\n\
                                <elementProp name=\"ThreadGroup.main_controller\" elementType=\"LoopController\" guiclass=\"LoopControlPanel\" testclass=\"LoopController\" testname=\"Loop Controller\" enabled=\"true\">\n\
                                  <boolProp name=\"LoopController.continue_forever\">false</boolProp>\n\
                                  <stringProp name=\"LoopController.loops\">100</stringProp>\n\
                                </elementProp>\n\
                                <stringProp name=\"ThreadGroup.num_threads\">"+ str(v) +"</stringProp>\n\
                                <stringProp name=\"ThreadGroup.ramp_time\">10</stringProp>\n\
                                <boolProp name=\"ThreadGroup.scheduler\">false</boolProp>\n\
                                <stringProp name=\"ThreadGroup.duration\"></stringProp>\n\
                                <stringProp name=\"ThreadGroup.delay\"></stringProp>\n\
                                <boolProp name=\"ThreadGroup.same_user_on_next_iteration\">true</boolProp>\n\
                              </ThreadGroup>\n\
                              <hashTree>\n"
                    xmlfile.write(str(concurrency))
                if k=="TestThroughput":
                    TestThroughput="<ConstantThroughputTimer guiclass=\"TestBeanGUI\" testclass=\"ConstantThroughputTimer\" testname=\"Constant Throughput Timer\" enabled=\"true\">\n\
                                  <intProp name=\"calcMode\">0</intProp>\n\
                                  <doubleProp>\n\
                                    <name>throughput</name>\n\
                                    <value>"+ str(v) +"</value>\n\
                                    <savedValue>0.0</savedValue>\n\
                                  </doubleProp>\n\
                                </ConstantThroughputTimer>\n\
                                <hashTree/>\n\
                                <IncludeController guiclass=\"IncludeControllerGui\" testclass=\"IncludeController\" testname=\"Include Controller\" enabled=\"false\">\n\
                                  <stringProp name=\"IncludeController.includepath\"></stringProp>\n\
                                </IncludeController>\n\
                                <hashTree/>\n\
                                <ConfigTestElement guiclass=\"HttpDefaultsGui\" testclass=\"ConfigTestElement\" testname=\"HTTP Request Defaults\" enabled=\"true\">\n\
                                  <elementProp name=\"HTTPsampler.Arguments\" elementType=\"Arguments\" guiclass=\"HTTPArgumentsPanel\" testclass=\"Arguments\" testname=\"User Defined Variables\" enabled=\"true\">\n\
                                    <collectionProp name=\"Arguments.arguments\"/>\n\
                                  </elementProp>\n\
                                  <stringProp name=\"HTTPSampler.domain\"></stringProp>\n\
                                  <stringProp name=\"HTTPSampler.port\"></stringProp>\n\
                                  <stringProp name=\"HTTPSampler.protocol\"></stringProp>\n\
                                  <stringProp name=\"HTTPSampler.contentEncoding\"></stringProp>\n\
                                  <stringProp name=\"HTTPSampler.path\"></stringProp>\n\
                                  <stringProp name=\"HTTPSampler.concurrentPool\">6</stringProp>\n\
                                  <stringProp name=\"HTTPSampler.connect_timeout\"></stringProp>\n\
                                  <stringProp name=\"HTTPSampler.response_timeout\"></stringProp>\n</ConfigTestElement>\n\
                                <hashTree/>\n\
                                <CSVDataSet guiclass=\"TestBeanGUI\" testclass=\"CSVDataSet\" testname=\"CSV Data Set Config\" enabled=\"true\">\n\
                                  <stringProp name=\"delimiter\">,</stringProp>\n\
                                  <stringProp name=\"fileEncoding\"></stringProp>\n\
                                  <stringProp name=\"filename\"></stringProp>\n\
                                  <boolProp name=\"ignoreFirstLine\">false</boolProp>\n\
                                  <boolProp name=\"quotedData\">false</boolProp>\n\
                                  <boolProp name=\"recycle\">true</boolProp>\n\
                                  <stringProp name=\"shareMode\">shareMode.all</stringProp>\n\
                                  <boolProp name=\"stopThread\">false</boolProp>\n\
                                  <stringProp name=\"variableNames\"></stringProp>\n\
                                </CSVDataSet>\n\
                                <hashTree/>\n\
                                <CookieManager guiclass=\"CookiePanel\" testclass=\"CookieManager\" testname=\"HTTP Cookie Manager\" enabled=\"true\">\n\
                                  <collectionProp name=\"CookieManager.cookies\"/>\n\
                                  <boolProp name=\"CookieManager.clearEachIteration\">false</boolProp>\n\
                                  <boolProp name=\"CookieManager.controlledByThreadGroup\">false</boolProp>\n\
                                </CookieManager>\n\
                                <hashTree/>\n\
                                <CacheManager guiclass=\"CacheManagerGui\" testclass=\"CacheManager\" testname=\"HTTP Cache Manager\" enabled=\"true\">\n\
                                  <boolProp name=\"clearEachIteration\">false</boolProp>\n\
                                  <boolProp name=\"useExpires\">true</boolProp>\n\
                                  <boolProp name=\"CacheManager.controlledByThread\">false</boolProp>\n\
                                </CacheManager>\n\
                                <hashTree/>\n"
                    xmlfile.write(str(TestThroughput))
                if k=="Threads":
                    for thread in my_dict['Threads']:
                        for x in enumerate(thread.items()):
                            thread="<ThroughputController guiclass=\"ThroughputControllerGui\" testclass=\"ThroughputController\" testname=\""+ str(x[1][1]['ThreadName']) +" - Throughput Controller\" enabled=\"true\">\n\
                                  <intProp name=\"ThroughputController.style\">1</intProp>\n\
                                  <boolProp name=\"ThroughputController.perThread\">false</boolProp>\n\
                                  <intProp name=\"ThroughputController.maxThroughput\">1</intProp>\n\
                                  <FloatProperty>\n\
                                    <name>ThroughputController.percentThroughput</name>\n\
                                    <value>"+ str(x[1][1]['Throughput'])+ "</value>\n\
                                    <savedValue>0.0</savedValue>\n\
                                  </FloatProperty>\n\
                                </ThroughputController>\n\
                                <hashTree>\n\
                                  <HTTPSamplerProxy guiclass=\"HttpTestSampleGui\" testclass=\"HTTPSamplerProxy\" testname=\""+ str(x[1][1]['ThreadName']) +"\" enabled=\"true\">\n\
                                    <elementProp name=\"HTTPsampler.Arguments\" elementType=\"Arguments\" guiclass=\"HTTPArgumentsPanel\" testclass=\"Arguments\" testname=\"User Defined Variables\" enabled=\"true\">\n\
                                      <collectionProp name=\"Arguments.arguments\"/>\n\
                                    </elementProp>\n\
                                    <stringProp name=\"HTTPSampler.domain\"></stringProp>\n\
                                    <stringProp name=\"HTTPSampler.port\"></stringProp>\n\
                                    <stringProp name=\"HTTPSampler.protocol\"></stringProp>\n\
                                    <stringProp name=\"HTTPSampler.contentEncoding\"></stringProp>\n\
                                    <stringProp name=\"HTTPSampler.path\"></stringProp>\n\
                                    <stringProp name=\"HTTPSampler.method\">"+ str(x[1][1]['Method'])+ "</stringProp>\n\
                                    <boolProp name=\"HTTPSampler.follow_redirects\">true</boolProp>\n\
                                    <boolProp name=\"HTTPSampler.auto_redirects\">false</boolProp>\n\
                                    <boolProp name=\"HTTPSampler.use_keepalive\">true</boolProp>\n\
                                    <boolProp name=\"HTTPSampler.DO_MULTIPART_POST\">false</boolProp>\n\
                                    <stringProp name=\"HTTPSampler.embedded_url_re\"></stringProp>\n\
                                    <stringProp name=\"HTTPSampler.connect_timeout\"></stringProp>\n\
                                    <stringProp name=\"HTTPSampler.response_timeout\"></stringProp>\n\
                                  </HTTPSamplerProxy>\n\
                                  <hashTree>\n\
                                    <ResponseAssertion guiclass=\"AssertionGui\" testclass=\"ResponseAssertion\" testname=\"Response Assertion\" enabled=\"true\">\n\
                                      <collectionProp name=\"Asserion.test_strings\">\n\
                                        <stringProp name=\"49586\">200</stringProp>\n\
                                      </collectionProp>\n\
                                      <stringProp name=\"Assertion.custom_message\"></stringProp>\n\
                                      <stringProp name=\"Assertion.test_field\">Assertion.response_code</stringProp>\n\
                                      <boolProp name=\"Assertion.assume_success\">false</boolProp>\n\
                                      <intProp name=\"Assertion.test_type\">16</intProp>\n\
                                    </ResponseAssertion>\n\
                                  <hashTree/>\n\
                                  <HeaderManager guiclass=\"HeaderPanel\" testclass=\"HeaderManager\" testname=\"HTTP Header Manager\" enabled=\"true\">\n\
                                      <collectionProp name=\"HeaderManager.headers\"/>\n\
                                    </HeaderManager>\n\
                                    <hashTree/>\n\
                                  </hashTree>\n\
                                </hashTree>\n"
                        xmlfile.write(str(thread))
        summary="<ResultCollector guiclass=\"SummaryReport\" testclass=\"ResultCollector\" testname=\"Summary Report\" enabled=\"true\">\n\
                  <boolProp name=\"ResultCollector.error_logging\">false</boolProp>\n\
                  <objProp>\n\
                    <name>saveConfig</name>\n\
                    <value class=\"SampleSaveConfiguration\">\n\
                      <time>true</time>\n\
                      <latency>true</latency>\n\
                      <timestamp>true</timestamp>\n\
                      <success>true</success>\n\
                      <label>true</label>\n\
                      <code>true</code>\n\
                      <message>true</message>\n\
                      <threadName>true</threadName>\n\
                      <dataType>true</dataType>\n\
                      <encoding>false</encoding>\n\
                      <assertions>true</assertions>\n\
                      <subresults>true</subresults>\n\
                      <responseData>false</responseData>\n\
                      <samplerData>false</samplerData>\n\
                      <xml>false</xml>\n\
                      <fieldNames>true</fieldNames>\n\
                      <responseHeaders>false</responseHeaders>\n\
                      <requestHeaders>false</requestHeaders>\n\
                      <responseDataOnError>false</responseDataOnError>\n\
                      <saveAssertionResultsFailureMessage>true</saveAssertionResultsFailureMessage>\n\
                      <assertionsResultsToSave>0</assertionsResultsToSave>\n\
                      <bytes>true</bytes>\n\
                      <sentBytes>true</sentBytes>\n\
                      <url>true</url>\n\
                      <threadCounts>true</threadCounts>\n\
                      <idleTime>true</idleTime>\n\
                      <connectTime>true</connectTime>\n\
                    </value>\n\
                  </objProp>\n\
                  <stringProp name=\"filename\"></stringProp>\n\
                </ResultCollector>\n\
                <hashTree/>\n\
              </hashTree>\n\
              <BackendListener guiclass=\"BackendListenerGui\" testclass=\"BackendListener\" testname=\"Backend Listener\" enabled=\"false\">\n\
                <elementProp name=\"arguments\" elementType=\"Arguments\" guiclass=\"ArgumentsPanel\" testclass=\"Arguments\" enabled=\"true\">\n\
                  <collectionProp name=\"Arguments.arguments\">\n\
                    <elementProp name=\"graphiteMetricsSender\" elementType=\"Argument\">\n\
                      <stringProp name=\"Argument.name\">graphiteMetricsSender</stringProp>\n\
                      <stringProp name=\"Argument.value\">org.apache.jmeter.visualizers.backend.graphite.TextGraphiteMetricsSender</stringProp>\n\
                      <stringProp name=\"Argument.metadata\">=</stringProp>\n\
                    </elementProp>\n\
                    <elementProp name=\"graphiteHost\" elementType=\"Argument\">\n\
                      <stringProp name=\"Argument.name\">graphiteHost</stringProp>\n\
                      <stringProp name=\"Argument.value\"></stringProp>\n\
                      <stringProp name=\"Argument.metadata\">=</stringProp>\n\
                    </elementProp>\n\
                    <elementProp name=\"graphitePort\" elementType=\"Argument\">\n\
                      <stringProp name=\"Argument.name\">graphitePort</stringProp>\n\
                      <stringProp name=\"Argument.value\">2003</stringProp>\n\
                      <stringProp name=\"Argument.metadata\">=</stringProp>\n\
                    </elementProp>\n\
                    <elementProp name=\"rootMetricsPrefix\" elementType=\"Argument\">\n\
                      <stringProp name=\"Argument.name\">rootMetricsPrefix</stringProp>\n\
                      <stringProp name=\"Argument.value\">jmeter.</stringProp>\n\
                      <stringProp name=\"Argument.metadata\">=</stringProp>\n\
                    </elementProp>\n\
                    <elementProp name=\"summaryOnly\" elementType=\"Argument\">\n\
                      <stringProp name=\"Argument.name\">summaryOnly</stringProp>\n\
                      <stringProp name=\"Argument.value\">true</stringProp>\n\
                      <stringProp name=\"Argument.metadata\">=</stringProp>\n\
                    </elementProp>\n\
                    <elementProp name=\"samplersList\" elementType=\"Argument\">\n\
                      <stringProp name=\"Argument.name\">samplersList</stringProp>\n\
                      <stringProp name=\"Argument.value\"></stringProp>\n\
                      <stringProp name=\"Argument.metadata\">=</stringProp>\n\
                    </elementProp>\n\
                    <elementProp name=\"percentiles\" elementType=\"Argument\">\n\
                      <stringProp name=\"Argument.name\">percentiles</stringProp>\n\
                      <stringProp name=\"Argument.value\">90;95;99</stringProp>\n\
                      <stringProp name=\"Argument.metadata\">=</stringProp>\n\
                    </elementProp>\n\
                  </collectionProp>\n\
                </elementProp>\n\
                <stringProp name=\"classname\">org.apache.jmeter.visualizers.backend.graphite.GraphiteBackendListenerClient</stringProp>\n\
              </BackendListener>\n\
              <hashTree/>\n\
            </hashTree>\n\
          </hashTree>\n\
        </jmeterTestPlan>\n"
        xmlfile.write(summary)
    xmlfile.close()
                    