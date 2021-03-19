+++
type = "question"
title = "Extracting Segmented SOAP XML Payload"
description = '''The following script:http://ask.wireshark.org/questions/4639/extracting-soap-xml-payload/4835 allows extracting soap messages. However, it fails to do so when the message is distributed over several TCP segments. Any hint to solve this problem?'''
date = "2013-01-29T09:50:00Z"
lastmod = "2013-02-11T11:33:00Z"
weight = 18046
keywords = [ "lua", "http", "desegment", "soap", "tshark" ]
aliases = [ "/questions/18046" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting Segmented SOAP XML Payload](/questions/18046/extracting-segmented-soap-xml-payload)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18046-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18046-score" class="post-score" title="current number of votes">0</div><span id="post-18046-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The following script:<a href="http://ask.wireshark.org/questions/4639/extracting-soap-xml-payload/4835">http://ask.wireshark.org/questions/4639/extracting-soap-xml-payload/4835</a> allows extracting soap messages. However, it fails to do so when the message is distributed over several TCP segments. Any hint to solve this problem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-desegment" rel="tag" title="see questions tagged &#39;desegment&#39;">desegment</span> <span class="post-tag tag-link-soap" rel="tag" title="see questions tagged &#39;soap&#39;">soap</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '13, 09:50</strong></p><img src="https://secure.gravatar.com/avatar/4761fd0cb20e397fc83df3e67bde3864?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="masgad&#39;s gravatar image" /><p><span>masgad</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="masgad has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Jan '13, 10:30</strong> </span></p></div></div><div id="comments-container-18046" class="comments-container"><span id="18258"></span><div id="comment-18258" class="comment"><div id="post-18258-score" class="comment-score"></div><div class="comment-text"><p>Please upload a sample capture on <a href="http://cloudshark.org">http://cloudshark.org</a>, and post a link here. What version of tshark are you using?</p></div><div id="comment-18258-info" class="comment-info"><span class="comment-age">(03 Feb '13, 10:30)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="18277"></span><div id="comment-18277" class="comment"><div id="post-18277-score" class="comment-score"></div><div class="comment-text"><p>Thank you helloworld for your reply. tshark version: 1.9.0 and there you go a sample pcap: <a href="http://cloudshark.org/captures/74a6deb7aa4e">http://cloudshark.org/captures/74a6deb7aa4e</a></p></div><div id="comment-18277-info" class="comment-info"><span class="comment-age">(04 Feb '13, 06:29)</span> <span class="comment-user userinfo">masgad</span></div></div></div><div id="comment-tools-18046" class="comment-tools"></div><div class="clear"></div><div id="comment-18046-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18304"></span>

<div id="answer-container-18304" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18304-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18304-score" class="post-score" title="current number of votes">1</div><span id="post-18304-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The original Lua script pulls out TCP data in raw form. In your case, your payload is encoded, so the raw form looks like gibberish.</p><p>To work with your packet capture, change the first 3 lines of the Lua script to the following:</p><pre><code>-- tap uses dfilter for HTTP and XML, where SOAP content is found
local tap       = Listener.new(nil, &quot;http &amp;&amp; xml&quot;)
local xml_field = Field.new(&quot;xml&quot;)</code></pre><p>I must admit this Lua script is a bit "hacky".</p><p>I recommend checking out <a href="http://www.wireshark.org/docs/man-pages/tshark.html#z_follow_prot_mode_filter_range"><code>tshark -z follow,tcp,ascii,STREAM</code></a> combined with a little scripting (<code>bash</code>, <code>awk</code>, <code>python</code>, etc). For instance, the following <code>bash</code> script dumps the SOAP streams from your pcap to individual files (one per stream). Further scripting is necessary to clean out the non-SOAP text from the files.</p><pre><code>#!/bin/bash

TSHARK=$HOME/src/wireshark/tshark
PCAP=$HOME/tmp/sample.pcap

# write the streams to individual files
while read stream
do
    echo &quot;writing stream $stream --&gt; $stream.txt&quot;
    $TSHARK -qz follow,tcp,ascii,$stream -r $PCAP &gt; $stream.txt
done &lt; &lt;($TSHARK -T fields -e tcp.stream -r $PCAP | sort | uniq)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '13, 22:13</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-18304" class="comments-container"><span id="18325"></span><div id="comment-18325" class="comment"><div id="post-18325-score" class="comment-score"></div><div class="comment-text"><p>I tried the two suggestions above. The first one (i.e., using "http &amp;&amp; xml" filter in the Listener) still missing a lot of xml SOAP messages. Dsipite capturing more SOAP messages, the script still missing SOAP messages besides that its output requires more cleaning to strip off non SOAP text. I am working on a workaround and I will post it later. Thank you.</p></div><div id="comment-18325-info" class="comment-info"><span class="comment-age">(05 Feb '13, 13:21)</span> <span class="comment-user userinfo">masgad</span></div></div><span id="18353"></span><div id="comment-18353" class="comment"><div id="post-18353-score" class="comment-score"></div><div class="comment-text"><p>Which packets in your sample.pcap contain the missing messages from the output?</p></div><div id="comment-18353-info" class="comment-info"><span class="comment-age">(05 Feb '13, 22:46)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="18494"></span><div id="comment-18494" class="comment"><div id="post-18494-score" class="comment-score"></div><div class="comment-text"><p>The Lua script cannot extract SOAP parts from segmented PDUs except the last one. I think that it couldn't identify them as xml or http. I noticed that wireshark's GUI also sees only the last packet as HTTP/XML whereas the previous packets are identified as TCP.</p></div><div id="comment-18494-info" class="comment-info"><span class="comment-age">(11 Feb '13, 10:34)</span> <span class="comment-user userinfo">masgad</span></div></div></div><div id="comment-tools-18304" class="comment-tools"></div><div class="clear"></div><div id="comment-18304-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18505"></span>

<div id="answer-container-18505" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18505-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18505-score" class="post-score" title="current number of votes">0</div><span id="post-18505-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I made a dirty workaround on the code from this post: <a href="http://ask.wireshark.org/questions/4639/extracting-soap-xml-payload/4835">http://ask.wireshark.org/questions/4639/extracting-soap-xml-payload/4835</a> The modified code differs from the original one in the following:</p><ol><li>It sets the Listener's filter to tcp rather than http or xml</li><li>It creates two separate Field extractors:</li></ol><p>local xml_field = Field.new("xml")</p><p>local tcp_segment = Field.new("tcp.data")</p><ol><li><p>It checks whether the analyzed packet contains any segemented PDU, and if so it will append the its contents in soap_message.</p></li><li><p>Every time it checks if the soap_message contains both beginning and closing tags. If yes, it flushes the soap_message before begin processing the next packet.</p></li></ol><p>The problem with this work around, is that sometimes it produces incorrect reassembly where it appends PDU contents from other packets if it happens to arrive in between as far as the soap message was not complete :(</p><p>Here is the code:</p><pre><code>-- tap uses filter for tcp and ignores retransmissions
local tap       = Listener.new(nil, &quot;tcp &amp;&amp; !tcp.analysis.retransmission&quot;)
-- XML field extractor
local xml_field = Field.new(&quot;xml&quot;)
-- TCP segment data extractor
local tcp_segment = Field.new(&quot;tcp.data&quot;)
local file      = nil
local soap_message = &#39;&#39;

-- #######################################################################
-- # If not already open, this opens a file for writing (append mode)
-- #######################################################################
local function open_file()
    if not file then
        local path = &quot;.&quot; .. &quot;/temp.xml&quot;
        print(&quot;opening file:&quot;, path)
        file = assert(io.open(path, &quot;a&quot;),
                    &quot;Can&#39;t open file for writing&quot;)
    end
end

local HTML_REQ = {
    [&quot;HTTP&quot;] = 1,
    [&quot;GET &quot;] = 1,
    [&quot;PUT &quot;] = 1,
    [&quot;POST&quot;] = 1,
}

-- #######################################################################
-- # Extracts the XML field from the buffer and writes the field to file
-- #######################################################################
local function handle_xml(pinfo, tvb)
    if not file then
        print(&quot;no file...ignoring packet&quot;)
        return
    end
    -- extract xml data if contained in single packet
    local data = &#39;&#39;
    local fieldinfo = xml_field()
    local segmentinfo = tcp_segment()
-- Check for PDUs
    if segmentinfo  then
        segmentdata = tvb(segmentinfo.offset):string()
        data = segmentdata
    elseif fieldinfo then
         xmldata   = tvb(fieldinfo.offset):string()
         data = xmldata
    end
    local starts = data:sub(1,4)
    -- some of these packets start w/HTTP header...skip to XML
    if HTML_REQ[starts] ~= nil then
--        local pos = string.find(xmldata, &quot;&lt;%?xml version&quot;)
        local pos = string.find(data, &quot;&lt;soap:Envelope&quot;)
        if not pos then
            return
        end
        data = data:sub(pos)
    end

    soap_message = soap_message .. data

    print(&quot;\n\n-- #&quot;..pinfo.number..&quot; ---------------------------------------------------\n&quot;)
    print(data)

    local soap_begin = string.find(soap_message, &quot;&lt;soap:Envelope&quot;)
    local soap_end = string.find(soap_message, &quot;&lt;/soap:Envelope&gt;&quot;)

-- Check for a the completion of the soap meassage
    if  soap_begin and soap_end then
        file:write(&quot;\n\n-- #&quot;..pinfo.number..&quot; ---------------------------------------------------\n&quot;)
        file:write(soap_message)
        soap_message = &#39;&#39;
    end
end

-- #######################################################################
-- # tap.packet() is called to notify the Listener of a packet that
-- # matches its filter rule (&quot;xml&quot; in this case). This can be called
-- # multiple times before tap.draw().
-- #######################################################################
-- #######################################################################
-- # tap.packet() is called to notify the Listener of a packet that
-- # matches its filter rule (&quot;xml&quot; in this case). This can be called
-- # multiple times before tap.draw().
-- #######################################################################
function tap.packet(pinfo, tvb)
    print(&quot;\ntap.packet&quot;, &quot;#&quot;..pinfo.number)

    -- XXX: Compensate for no tap.reset() in tshark
    if not gui_enabled() then open_file() end

    -- wrap the handler in a pcall() in case an error occurs
    local ok, msg = pcall(  function()
                                handle_xml(pinfo,tvb)
                            end )

    -- print any error and bow out
    if not ok then
        print(&quot;wtf!&quot;, msg)
    end

end

-- #######################################################################
-- # tap.draw() is called to notify the Listener to &quot;draw&quot; its results
-- # that were accumulated in tap.packet(). This is normally called after
-- # tap.packet(), based on &quot;Preferences &gt; Statistics &gt; Tap update interval&quot;.
-- #######################################################################
function tap.draw()
    print(&quot;tap.draw&quot;)
    -- flush toilet (NOTE: When $file is garbage collected, it&#39;s
    -- automatically flushed and closed...that doesn&#39;t mean we
    -- can&#39;t do it sooner to free resources.)
    if file then
        print(&quot;closing file&quot;)
        file:close()
        file = nil
    end
end

-- #######################################################################
-- # tap.reset() is called to notify the Listener to reset any variables
-- # or counters in preparation for a packet (passed to tap.packet()).
-- # This can be called multiple times before a packet is even seen.
-- #
-- # XXX: tshark doesn&#39;t call this function, but Wireshark does. Bug?
-- #######################################################################
function tap.reset()
    print(&quot;tap.reset&quot;)
    open_file()
end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '13, 11:33</strong></p><img src="https://secure.gravatar.com/avatar/4761fd0cb20e397fc83df3e67bde3864?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="masgad&#39;s gravatar image" /><p><span>masgad</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="masgad has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Feb '13, 12:17</strong> </span></p></div></div><div id="comments-container-18505" class="comments-container"></div><div id="comment-tools-18505" class="comment-tools"></div><div class="clear"></div><div id="comment-18505-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

