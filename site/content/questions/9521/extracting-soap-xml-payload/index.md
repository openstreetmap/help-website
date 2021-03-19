+++
type = "question"
title = "Extracting SOAP XML Payload"
description = '''I am referring to a thread already answered last summer - http://ask.wireshark.org/questions/4639/extracting-soap-xml-payload?sort=votes&amp;amp;page=1 I got this script working reading off of a pcap with: tshark -r &quot;/tmp/test.pcap&quot; &quot;tcp and data&quot; -X lua_script:/tmp/luaListener.lua  Now, I am having a p...'''
date = "2012-03-13T12:49:00Z"
lastmod = "2012-03-14T19:55:00Z"
weight = 9521
keywords = [ "xml", "lua", "pcap", "soap", "tshark" ]
aliases = [ "/questions/9521" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting SOAP XML Payload](/questions/9521/extracting-soap-xml-payload)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9521-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am referring to a thread already answered last summer - <a href="http://ask.wireshark.org/questions/4639/extracting-soap-xml-payload?sort=votes&amp;page=1">http://ask.wireshark.org/questions/4639/extracting-soap-xml-payload?sort=votes&amp;page=1</a></p><p>I got this <a href="http://ask.wireshark.org/questions/4639/extracting-soap-xml-payload?page=1#4835">script</a> working reading off of a pcap with:</p><pre><code>tshark -r &quot;/tmp/test.pcap&quot; &quot;tcp and data&quot; -X lua_script:/tmp/luaListener.lua</code></pre><p>Now, I am having a problem running the Lua script on a live capture (here's a <a href="http://cloudshark.org/captures/e11c1401507b">sample pcap</a>). In the Lua file, I have <code>tap</code> set to <code>xml</code> and <code>field</code> set to <code>xml</code>. Here is my command prompt:</p><pre><code>tshark &quot;tcp and data&quot; -X lua_script:/tmp/luaListener.lua -i lo</code></pre><p>When I run this, I get a stream of data on the screen, but the listener is not picking up anything, and the file is not created. Can anyone help?</p></div><div id="question-tags" class="tags-container tags">xml lua pcap soap tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '12, 12:49</strong></p><img src="https://secure.gravatar.com/avatar/99064d4d0553530d9de8096e634dc5c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pilotgurl86&#39;s gravatar image" /><p>pilotgurl86<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pilotgurl86 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Mar '12, 15:03</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-9521" class="comments-container"><span id="9522"></span><div id="comment-9522" class="comment"><div id="post-9522-score" class="comment-score"></div><div class="comment-text"><p>Sorry I had a typo - the last command line is supposed to be;</p><p>tshark -R "tcp and data" -X lua_script:/tmp/luaListenr.lua -i lo</p></div><div id="comment-9522-info" class="comment-info"><span class="comment-age">(13 Mar '12, 12:51)</span> pilotgurl86</div></div></div><div id="comment-tools-9521" class="comment-tools"></div><div class="clear"></div><div id="comment-9521-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9548"></span>

<div id="answer-container-9548" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9548-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The filter <code>"tcp and data"</code> does not apply to your pcap. That is, your SOAP XML packets are not contained in TCP packets as <code>data</code> fields as they were in the original post. I'm not sure if that's because of a change in the dissector or because the SOAP XML is generated differently for you than for the author of that post, but you can achieve the same results by changing the tap filter and <code>Field</code> from <code>"data"</code> to <code>"xml"</code>:</p><pre><code>-- tap uses dfilter for tcp data and ignores retransmissions
local tap       = Listener.new(nil, &quot;tcp &amp;&amp; dataxml &amp;&amp; !tcp.analysis.retransmission&quot;)
local xml_field = Field.new(&quot;data&quot;&quot;xml&quot;)</code></pre><p><br />
The result of this command:</p><pre><code>$ tshark -r /tmp/test.pcap -Xlua_script:/tmp/luaListener.lua &quot;xml&quot;</code></pre><p>creates the <code>temp.xml</code> file, containing:</p><pre><code>&lt;soap:Envelope xmlns:soap=&quot;http://www.w3.org/2003/05/soap-envelope&quot; xmlns:web=&quot;http://www.webserviceX.NET/&quot;&gt;
   &lt;soap:Header/&gt;
   &lt;soap:Body&gt;
      &lt;web:ConversionRate&gt;
         &lt;web:FromCurrency&gt;USD&lt;/web:FromCurrency&gt;
         &lt;web:ToCurrency&gt;CAD&lt;/web:ToCurrency&gt;
      &lt;/web:ConversionRate&gt;
   &lt;/soap:Body&gt;
&lt;/soap:Envelope&gt;

-- #6 ---------------------------------------------------

&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;&lt;soap:Envelope xmlns:soap=&quot;http://www.w3.org/2003/05/soap-envelope&quot; xmlns:xsi=&quot;http://www.w3.org/2001/XMLSchema-instance&quot; xmlns:xsd=&quot;http://www.w3.org/2001/XMLSchema&quot;&gt;&lt;soap:Body&gt;&lt;ConversionRateResponse xmlns=&quot;http://www.webserviceX.NET/&quot;&gt;&lt;ConversionRateResult&gt;0.991&lt;/ConversionRateResult&gt;&lt;/ConversionRateResponse&gt;&lt;/soap:Body&gt;&lt;/soap:Envelope&gt;

-- #8 ---------------------------------------------------

&lt;soapenv:Envelope xmlns:soapenv=&quot;http://schemas.xmlsoap.org/soap/envelope/&quot; xmlns:web=&quot;http://www.webserviceX.NET/&quot;&gt;
   &lt;soapenv:Header/&gt;
   &lt;soapenv:Body&gt;
      &lt;web:ConversionRate&gt;
         &lt;web:FromCurrency&gt;CAD&lt;/web:FromCurrency&gt;
         &lt;web:ToCurrency&gt;EUR&lt;/web:ToCurrency&gt;
      &lt;/web:ConversionRate&gt;
   &lt;/soapenv:Body&gt;
&lt;/soapenv:Envelope&gt;

-- #10 ---------------------------------------------------

&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;&lt;soap:Envelope xmlns:soap=&quot;http://schemas.xmlsoap.org/soap/envelope/&quot; xmlns:xsi=&quot;http://www.w3.org/2001/XMLSchema-instance&quot; xmlns:xsd=&quot;http://www.w3.org/2001/XMLSchema&quot;&gt;&lt;soap:Body&gt;&lt;ConversionRateResponse xmlns=&quot;http://www.webserviceX.NET/&quot;&gt;&lt;ConversionRateResult&gt;0.7711&lt;/ConversionRateResult&gt;&lt;/ConversionRateResponse&gt;&lt;/soap:Body&gt;&lt;/soap:Envelope&gt;

-- #12 ---------------------------------------------------</code></pre></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '12, 19:55</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Mar '12, 19:56</p></div></div><div id="comments-container-9548" class="comments-container"><span id="9552"></span><div id="comment-9552" class="comment"><div id="post-9552-score" class="comment-score"></div><div class="comment-text"><p>Thanks, that works great! How would you get this to run off of the network and not a pcap file? Just remove the pcap file? It doesn't seem to work, it will show traffic, but not record anything in the XML file.</p></div><div id="comment-9552-info" class="comment-info"><span class="comment-age">(15 Mar '12, 04:29)</span> pilotgurl86</div></div></div><div id="comment-tools-9548" class="comment-tools"></div><div class="clear"></div><div id="comment-9548-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

