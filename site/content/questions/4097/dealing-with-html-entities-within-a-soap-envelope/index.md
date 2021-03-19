+++
type = "question"
title = "Dealing with HTML entities within a SOAP envelope"
description = '''I&#x27;m capturing and decoding traffic within a SOAP envelope. The source application passes an XML payload through WCF which then converts all the XML reserved characters into HTML entities. So the less than symbol (&amp;lt;) becomes &amp;amp;lt;. And greater than becomes &amp;amp;gt; And so on and so forth accord...'''
date = "2011-05-16T18:33:00Z"
lastmod = "2011-06-10T14:36:00Z"
weight = 4097
keywords = [ "xml", "entities", "html", "soap" ]
aliases = [ "/questions/4097" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dealing with HTML entities within a SOAP envelope](/questions/4097/dealing-with-html-entities-within-a-soap-envelope)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4097-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4097-score" class="post-score" title="current number of votes">0</div><span id="post-4097-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm capturing and decoding traffic within a SOAP envelope. The source application passes an XML payload through WCF which then converts all the XML reserved characters into HTML entities. So the less than symbol <strong>(&lt;)</strong> becomes <code>&amp;lt;</code>. And greater than becomes <code>&amp;gt;</code> And so on and so forth according to W3C rules.</p><p>What I see in Wireshark is something like this:</p><pre><code>+Frame....
+Ethernet....
+Internet Protocol....
+Transmission Control....
+[Reassembled TCP Segments....
+Hypertext Transfer Protocol....
-eXtensible Markup Language
 +&lt;?xml
 -&lt;SOAP-ENV:Envelope....
  -&lt;SOAP-ENV:Body&gt;
   -&lt;g2s:g2sRequest&gt;
    -&lt;g2s:g2sRequest&gt;
     [truncated] &amp;lt;?&lt;xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&amp;gt;&amp;#xa;&amp;lt;g2s:g2sMessage....
     &lt;/g2s:g2sRequest&gt;
....</code></pre><p>The xml in the truncated line can be thousands of bytes long. But it contains fields that I need to do filtering and statistics on. I want to convert the HTML entities back to their original less than and greater than symbols, and then do filtering as I would with any XML document in Wireshark--something like gs2message A=10%, gs2message B=20%, etc. Of course, this would mean XML inside XML and I think the parser would have a fit. Why it wasn't put into a CDATA block to begin with, I don't know. But this is what I have to work with. So can I load it into a CDATA block instead within Wireshark and then reconstitute the XML for display, filtering, stats? And converting this back to real XML, wouldn't that mess up my byte size statistics? If within Wireshark would this be done with a dissector or DTD file? Is it even possible to reconstitute the XML payload within WireShark? Or do I have to do it after the fact?<br />
</p><p>If I go outside of Wireshark would something like Pilot work? Or do I need to write something custom in say Python? But at the same time, I still want all the Frame, Ethernet, TCP/IP info on data sizes for bandwith and latency analysis. It's just that the filtering fields are inside this locked up XML.</p><p>All advice is welcome.</p><p>Cheers NewbieBrian</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-entities" rel="tag" title="see questions tagged &#39;entities&#39;">entities</span> <span class="post-tag tag-link-html" rel="tag" title="see questions tagged &#39;html&#39;">html</span> <span class="post-tag tag-link-soap" rel="tag" title="see questions tagged &#39;soap&#39;">soap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '11, 18:33</strong></p><img src="https://secure.gravatar.com/avatar/6d70926a09a65b1329fb803549ab7205?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NewbieBrian&#39;s gravatar image" /><p><span>NewbieBrian</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NewbieBrian has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 May '11, 14:16</strong> </span></p></div></div><div id="comments-container-4097" class="comments-container"></div><div id="comment-tools-4097" class="comment-tools"></div><div class="clear"></div><div id="comment-4097-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4516"></span>

<div id="answer-container-4516" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4516-score" class="post-score" title="current number of votes">0</div><span id="post-4516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have a solution.</p><p>It turns out that my application payload data, the line above that says [truncated] &lt;?xml...... Well, if the XML dissector has already executed, this data will be held inside of the field <strong>xml.cdata</strong> By using a Post Dissector (thereby insuring that the HTTP and XML dissectors have executed), you can steal the payload from xml.cdata, sun a series of substitutions to put it back into XML form, and now you're ready to process your application data.</p><p>The steps are:</p><pre><code>--Creat local field for xml.cdata
f_xml_cdata = Field.new(&quot;xml.cdata&quot;)
.....
function trivial_proto.dissector(buffer, pinfo, tree)
     --Put field data into local variable inside
     local l_xml_cdata = f_xml_cdata()
     --Check to see if we have xml payload otherwise return
     if l_xml_cdata == nil then return end
     --Convert to String
     s_xml_cdata = tostring(l_xml_cdata)
     .....
     --Substitute HTML entities for real XML reserved characters
     s_xml_cdata = string.gsub(s_xml_cdata, &quot;&amp;lt;&quot;, &quot;&lt;&quot;)
     s_xml_cdata = string.gsub(s_xml_cdata, &quot;&amp;gt;&quot;, &quot;&gt;&quot;)
     --Convert \r to nothing
     s_xml_cdata = string.gsub(s_xml_cdata, &quot;&amp;#xA;&quot;, &quot;&quot;)
     --Convert \n to nothing
     s_xml_cdata = string.gsub(s_xml_cdata, &quot;&amp;#xD;&quot;, &quot;&quot;)
     --In case some systems don&#39;t leave real linefeeds in, convert them to nothing
     s_xml_cdata = string.gsub(s_xml_cdata, &quot;\n&quot;, &quot;&quot;)
     --Optional statement to get rid of any leading spaces between nodes
     s_xml_cdata = string.gsub(s_xml_cdata, &quot;%s*&lt;&quot;, &quot;&lt;&quot;)</code></pre><p>Hope this was helpful</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '11, 14:36</strong></p><img src="https://secure.gravatar.com/avatar/6d70926a09a65b1329fb803549ab7205?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NewbieBrian&#39;s gravatar image" /><p><span>NewbieBrian</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NewbieBrian has no accepted answers">0%</span></p></div></div><div id="comments-container-4516" class="comments-container"></div><div id="comment-tools-4516" class="comment-tools"></div><div class="clear"></div><div id="comment-4516-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

