+++
type = "question"
title = "lua tap and multiple instances of a protocol in one frame"
description = '''I&#x27;ve got following situation in one frame in my capture file Frame  ethernet  IP  SCTP -&amp;gt; MTP3 -&amp;gt; *SCCP* -&amp;gt; TCAP -&amp;gt; INAP  SCTP -&amp;gt; MTP3 -&amp;gt; SCCP -&amp;gt; TCAP -&amp;gt; INAP  SCTP -&amp;gt; MTP3 -&amp;gt; _SCCP_ -&amp;gt; TCAP -&amp;gt; _CAP_  I want to extract information from _CAP_ and _SCCP_ (both marke...'''
date = "2012-05-15T12:18:00Z"
lastmod = "2012-05-16T06:05:00Z"
weight = 11000
keywords = [ "lua", "sigtran", "tap", "camel" ]
aliases = [ "/questions/11000" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [lua tap and multiple instances of a protocol in one frame](/questions/11000/lua-tap-and-multiple-instances-of-a-protocol-in-one-frame)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11000-score" class="post-score" title="current number of votes">0</div><span id="post-11000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've got following situation in one frame in my capture file</p><pre><code>Frame
  ethernet
    IP
      SCTP -&gt; MTP3 -&gt; *SCCP* -&gt; TCAP -&gt; INAP
      SCTP -&gt; MTP3 -&gt; SCCP -&gt; TCAP -&gt; INAP
      SCTP -&gt; MTP3 -&gt; _SCCP_ -&gt; TCAP -&gt; _CAP_</code></pre><p>I want to extract information from <code>_CAP_</code> and <code>_SCCP_</code> (both marked with underscore above) I used following extractors</p><pre><code>called_party_msisdn_extractor = Field.new(&quot;e164.called_party_number.digits&quot;)
calling_party_msisdn_extractor = Field.new(&quot;e164.calling_party_number.digits&quot;)
sccp_called_gt = Field.new(&quot;sccp.called.digits&quot;)
sccp_calling_gt = Field.new(&quot;sccp.calling.digits&quot;)
frame_number = Field.new(&quot;frame.number&quot;)
frame_time = Field.new(&quot;frame.time_epoch&quot;)
service_key = Field.new(&quot;camel.serviceKey&quot;)</code></pre><p>But what I got was a data from <code>_CAP_</code> and <code>*SCCP*</code> (not from <code>_SCCP_</code>)</p><p>How to write a tap to make it possbile to get <code>_CAP_</code> and <code>_SCCP_</code></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-sigtran" rel="tag" title="see questions tagged &#39;sigtran&#39;">sigtran</span> <span class="post-tag tag-link-tap" rel="tag" title="see questions tagged &#39;tap&#39;">tap</span> <span class="post-tag tag-link-camel" rel="tag" title="see questions tagged &#39;camel&#39;">camel</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 May '12, 12:18</strong></p><img src="https://secure.gravatar.com/avatar/9f5a1001269517ce97c85ff8fbb57897?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tciops&#39;s gravatar image" /><p><span>tciops</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tciops has no accepted answers">0%</span></p></div></div><div id="comments-container-11000" class="comments-container"><span id="11002"></span><div id="comment-11002" class="comment"><div id="post-11002-score" class="comment-score"></div><div class="comment-text"><p>Please post a sample capture at <a href="http://cloudshark.org">http://cloudshark.org</a></p></div><div id="comment-11002-info" class="comment-info"><span class="comment-age">(15 May '12, 14:54)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="11028"></span><div id="comment-11028" class="comment"><div id="post-11028-score" class="comment-score"></div><div class="comment-text"><p>capture contains data which I don't want and am not allowed to send - real user traffic with all confidential data</p><p>Cannot post it anywhere sorry...</p></div><div id="comment-11028-info" class="comment-info"><span class="comment-age">(16 May '12, 01:18)</span> <span class="comment-user userinfo">tciops</span></div></div><span id="11031"></span><div id="comment-11031" class="comment"><div id="post-11031-score" class="comment-score"></div><div class="comment-text"><p>you could select 3-4 packets with no "compromising" data in it.</p></div><div id="comment-11031-info" class="comment-info"><span class="comment-age">(16 May '12, 01:38)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11034"></span><div id="comment-11034" class="comment"><div id="post-11034-score" class="comment-score"></div><div class="comment-text"><p>All I can do is post you a text representation of this frame without any vulnerable data Unless you know a way to modify a pcap file to change this data</p></div><div id="comment-11034-info" class="comment-info"><span class="comment-age">(16 May '12, 02:18)</span> <span class="comment-user userinfo">tciops</span></div></div><span id="11035"></span><div id="comment-11035" class="comment"><div id="post-11035-score" class="comment-score"></div><div class="comment-text"><p>you can try this: <a href="http://sourceforge.net/projects/powereditpcap/">http://sourceforge.net/projects/powereditpcap/</a> or any HEX editor, if you know exactly what data to change. Beware to not change the header data.</p><p>BTW: can you post the whole dissector code? If that's not the case, I think it will be hard to help.</p></div><div id="comment-11035-info" class="comment-info"><span class="comment-age">(16 May '12, 02:35)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11039"></span><div id="comment-11039" class="comment not_top_scorer"><div id="post-11039-score" class="comment-score"></div><div class="comment-text"><p>It's not possible to post it or even attach it here so here is the link <a href="http://cdn.anonfiles.com/1337162613946.txt">http://cdn.anonfiles.com/1337162613946.txt</a></p></div><div id="comment-11039-info" class="comment-info"><span class="comment-age">(16 May '12, 03:07)</span> <span class="comment-user userinfo">tciops</span></div></div><span id="11040"></span><div id="comment-11040" class="comment not_top_scorer"><div id="post-11040-score" class="comment-score"></div><div class="comment-text"><p>powereditcap doesn't know how to edit SS7 protocols I gave up, it's not that easy and it's not so urgent frame txt <a href="http://cdn.anonfiles.com/1337164422323.txt">http://cdn.anonfiles.com/1337164422323.txt</a></p></div><div id="comment-11040-info" class="comment-info"><span class="comment-age">(16 May '12, 03:38)</span> <span class="comment-user userinfo">tciops</span></div></div><span id="11041"></span><div id="comment-11041" class="comment not_top_scorer"><div id="post-11041-score" class="comment-score"></div><div class="comment-text"><p>It's hard to test the Lua Tap with the text file. Can you please upload the same information in binary form (pcap) to cloudshark (or if you like to <a href="http://anonfiles.com">anonfiles.com</a>).</p></div><div id="comment-11041-info" class="comment-info"><span class="comment-age">(16 May '12, 04:29)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-11000" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-11000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11042"></span>

<div id="answer-container-11042" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11042-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11042-score" class="post-score" title="current number of votes">1</div><span id="post-11042-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tciops has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If I understand the problem correctly, you're trying to fetch the last instance of <code>"e164.called_party_number.digits"</code> and <code>"e164.calling_party_number.digits"</code> in an SCCP packet from a tap. The <code>Field</code> extractor fetches all instances of the named field, and they're normally accessed in a <code>for</code> loop. Try this Lua:</p><pre><code>local logfile = &quot;CAP_IDP_DATA_&quot;..os.date(&quot;%Y%m%d&quot;)..&quot;.csv&quot;
io.output(logfile)

local called_party_msisdn_extractor = Field.new(&quot;e164.called_party_number.digits&quot;)
local calling_party_msisdn_extractor = Field.new(&quot;e164.calling_party_number.digits&quot;)
local sccp_called_gt = Field.new(&quot;sccp.called.digits&quot;)
local sccp_calling_gt = Field.new(&quot;sccp.calling.digits&quot;)

-- XXX: you don&#39;t need these frame fields. You can get them from pinfo.number and pinfo.abs_ts
--local frame_number = Field.new(&quot;frame.number&quot;)
--local frame_time = Field.new(&quot;frame.time_epoch&quot;)

local service_key = Field.new(&quot;camel.serviceKey&quot;)

io.write(&quot;FRAME|GT|SKEY|MSISDNs|TIME\n&quot;)

local tap_cap = Listener.new(nil,&quot;camel.local == 0&quot;)

-- Gets the last instance of a Field extractor.
-- Returns nil if nothing extracted.
local function last(field)
    local last_elem = nil

    -- no easy way to get last element of userdata,
    -- so iterate the returned values until it reaches
    -- the last element
    for _,f in ipairs({ field() }) do
        last_elem = f
    end

    return last_elem
end

function tap_cap.packet(pinfo,tvb)
    local calling = last(calling_party_msisdn_extractor)
    local called = last(called_party_msisdn_extractor)

    local called_gt = sccp_called_gt()
    local calling_gt = sccp_calling_gt()

    -- XXX: replaced field extractors with equivalent pinfo accessors
    --local frame_no = frame_number()
    --local frame_t = frame_time()
    local frame_no = pinfo.number
    local frame_t = string.format(&quot;%.9f&quot;, pinfo.abs_ts)

    local skey = service_key()

    io.write(tostring(frame_no) .. &quot;|&quot; .. tostring(calling_gt) .. &quot; -&gt; &quot; .. tostring(called_gt)
        .. &quot;|&quot; .. tostring(skey)
        .. &quot;|&quot; .. tostring(calling) .. &quot; &gt; &quot; .. tostring(called)
        .. &quot;|&quot; ..tostring(frame_t) .. &quot;\n&quot;)
end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '12, 04:50</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-11042" class="comments-container"><span id="11046"></span><div id="comment-11046" class="comment"><div id="post-11046-score" class="comment-score"></div><div class="comment-text"><p>Thanks helloworld. It's <em>almost</em> the thing I wanted to get.</p><p>If I change just a little the order of data in frame to look like this:</p><pre><code>Frame
  ethernet
    IP
     SCTP -&gt; MTP3 -&gt; SCCP -&gt; TCAP -&gt; INAP
     SCTP -&gt; MTP3 -&gt; SCCP -&gt; TCAP -&gt; CAP
     SCTP -&gt; MTP3 -&gt; SCCP -&gt; TCAP -&gt; INAP</code></pre><p>I would get last SCCP info and the CAP info I want. I need data from CAP and SCCP which encapsulates this CAP packet (using TCAP). So, I guess I will have to somehow master this looping proposition. I just need to compare it with <code>sccp.called.ssn</code>.</p></div><div id="comment-11046-info" class="comment-info"><span class="comment-age">(16 May '12, 06:05)</span> <span class="comment-user userinfo">tciops</span></div></div></div><div id="comment-tools-11042" class="comment-tools"></div><div class="clear"></div><div id="comment-11042-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

