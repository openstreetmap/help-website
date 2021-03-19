+++
type = "question"
title = "Display multiple PDUs in a TCP segment"
description = '''With lots of help, I now understand that a Lua dissector that is meant to extract multiple higher-level PDUs from a given TCP segment must implement its own loop. As an example, I have implemented such a dissector for the TRIVIAL protocol (see homemade packet capture). Running tshark shows: 1 0.0000...'''
date = "2014-03-10T05:42:00Z"
lastmod = "2014-03-10T08:15:00Z"
weight = 30642
keywords = [ "lua", "dissector", "packet-display" ]
aliases = [ "/questions/30642" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Display multiple PDUs in a TCP segment](/questions/30642/display-multiple-pdus-in-a-tcp-segment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30642-score" class="post-score" title="current number of votes">0</div><span id="post-30642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>With lots of help, <a href="http://ask.wireshark.org/questions/30529/does-reassembly-address-multiple-pdus-in-a-single-tcp-segment">I now understand</a> that a Lua dissector that is meant to extract multiple higher-level PDUs from a given TCP segment must implement its own loop. As an example, I have implemented such a dissector for the TRIVIAL protocol (<a href="https://www.cloudshark.org/captures/ef2f1bb3e67a">see homemade packet capture</a>). Running <code>tshark</code> shows:</p><pre><code>1 0.000000   10.1.1.1 6666 10.2.2.2     7777 TRIVIAL 68 Trivial Info
2 0.000001   10.1.1.1 6666 10.2.2.2     7777 TRIVIAL 60 Trivial Info</code></pre><p>By running <code>tshark -V</code>, I can see the (multiple) contained <code>Trivial Protocol Data</code> subtrees in these segments. Progress!</p><p>Is there any way to have the output of tshark show something like:</p><pre><code>1 0.000000   10.1.1.1 6666 10.2.2.2     7777 TRIVIAL 68 Trivial Info
1 0.000000   10.1.1.1 6666 10.2.2.2     7777 TRIVIAL 68 Trivial Info
1 0.000000   10.1.1.1 6666 10.2.2.2     7777 TRIVIAL 68 Trivial Info
2 0.000001   10.1.1.1 6666 10.2.2.2     7777 TRIVIAL 60 Trivial Info</code></pre><p>that is, one row per <code>TRIVIAL</code> PDU rather than one row per TCP segment?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-packet-display" rel="tag" title="see questions tagged &#39;packet-display&#39;">packet-display</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '14, 05:42</strong></p><img src="https://secure.gravatar.com/avatar/143ca820606b9b8df4a6441003ef1b53?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yotommy&#39;s gravatar image" /><p><span>yotommy</span><br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yotommy has no accepted answers">0%</span></p></div></div><div id="comments-container-30642" class="comments-container"></div><div id="comment-tools-30642" class="comment-tools"></div><div class="clear"></div><div id="comment-30642-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="30644"></span>

<div id="answer-container-30644" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30644-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30644-score" class="post-score" title="current number of votes">1</div><span id="post-30644-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="yotommy has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Th short answer: not currently.</p><p>I believe there have been some previous similar requests and some discussions about same.</p><p>Something like implementing an expandable "treeview" for a summary line ?</p><p>I think a Google search "site:wireshark.org ..." with some appropriate search terms may find the previous discussions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Mar '14, 05:52</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-30644" class="comments-container"><span id="30646"></span><div id="comment-30646" class="comment"><div id="post-30646-score" class="comment-score"></div><div class="comment-text"><p>Thanks - I found this: <a href="http://ask.wireshark.org/questions/13402/alternate-display-for-packet-list-pane">http://ask.wireshark.org/questions/13402/alternate-display-for-packet-list-pane</a> (which contains pointers to other similar discussion items). I guess a workaround is to have the dissector print out exactly the info I need, and add a display filter to wireshark that will effectively suppress the default output.</p></div><div id="comment-30646-info" class="comment-info"><span class="comment-age">(10 Mar '14, 06:05)</span> <span class="comment-user userinfo">yotommy</span></div></div></div><div id="comment-tools-30644" class="comment-tools"></div><div class="clear"></div><div id="comment-30644-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30652"></span>

<div id="answer-container-30652" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30652-score" class="post-score" title="current number of votes">1</div><span id="post-30652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Welll, well... it appears Lua can do something C-code can't. :)</p><p>Here's your Trivial dissector, with multi-line tshark output (you may need to tweak the makeLine function):</p><pre><code>-- declare our protocol
local trivial_proto = Proto(&quot;trivial&quot;,&quot;Trivial Protocol&quot;)

local trivial_pdu_len = 4
local makeLine

local function dissect_common(buffer, pinfo, tree, offset)

    local subtree = tree:add(trivial_proto,buffer(offset,trivial_pdu_len),&quot;Trivial Protocol Data&quot;)

    subtree:add(buffer(offset,2),&quot;The first two bytes: &quot; .. buffer(offset,2):uint())
    subtree = subtree:add(buffer(2,2),&quot;The next two bytes&quot;)
    subtree:add(buffer(offset+2,1),&quot;The 3rd byte: &quot; .. buffer(offset+2,1):uint())
    subtree:add(buffer(offset+3,1),&quot;The 4th byte: &quot; .. buffer(offset+3,1):uint())

    local output = &quot;Trivial Info (&quot; .. buffer(offset,2):uint() ..&quot;)&quot;

    -- return number of bytes consumed so that more trivial PDUs can be discovered
    return trivial_pdu_len, output
end

-- create a function to dissect it
function trivial_proto.dissector(buffer, pinfo, tree)   
    pinfo.cols.protocol = &quot;TRIVIAL&quot;

    local pktlen = buffer:len()

    local consumed, output = dissect_common(buffer, pinfo, tree, 0)
    local remaining = pktlen - consumed
    pinfo.cols.info:set(output)

    while remaining &gt;= trivial_pdu_len do
        consumed, output = dissect_common(buffer, pinfo, tree, pktlen - remaining)
        pinfo.cols.info:append(makeLine(pinfo,output))
        remaining = remaining - consumed
    end

    if remaining &gt; 0 then
        pinfo.desegment_offset = pktlen - remaining
        pinfo.desegment_len = trivial_pdu_len - remaining
    end

    return pktlen - remaining
end

-- load the tcp.port table
local tcp_table = DissectorTable.get(&quot;tcp.port&quot;)
-- register our protocol to handle udp port 7777
tcp_table:add(7777,trivial_proto)

-- helper function to enable multi-line packet output
makeLine = function (pinfo,output)
    local rel_time = string.format(&quot;%.6f\t&quot;, pinfo.rel_ts)

    local line = {
        &quot;\n &quot;,
        tostring(pinfo.number),
        rel_time,
        tostring(pinfo.src),
        tostring(pinfo.src_port),
        tostring(pinfo.dst),
        tostring(pinfo.dst_port),
        &quot;TRIVIAL&quot;,
        tostring(pinfo.len),
        output,
    }

    return table.concat(line,&quot; &quot;)
end</code></pre><p>Okay, okay... so I'm totally cheating. But hey it works! ;)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Mar '14, 07:36</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30652" class="comments-container"><span id="30654"></span><div id="comment-30654" class="comment"><div id="post-30654-score" class="comment-score"></div><div class="comment-text"><p>Very sneaky! Great, thanks for the help.</p></div><div id="comment-30654-info" class="comment-info"><span class="comment-age">(10 Mar '14, 08:15)</span> <span class="comment-user userinfo">yotommy</span></div></div></div><div id="comment-tools-30652" class="comment-tools"></div><div class="clear"></div><div id="comment-30652-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

