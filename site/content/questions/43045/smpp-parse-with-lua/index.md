+++
type = "question"
title = "SMPP parse with lua"
description = '''Hello! Sorry for my bad english! I write lua script for parse smpp protocol  do  local smpp_packets = 0  local tcp_ack_time_count = 0  local tcp_ack_time_sum = 0  local submit_sm = 0  local submit_sm_resp = 0  local deliver_sm = 0  local deliver_sm_resp = 0  local mo_deliver_sm = 0 local function in...'''
date = "2015-06-10T06:52:00Z"
lastmod = "2015-06-27T17:35:00Z"
weight = 43045
keywords = [ "smpp", "lua" ]
aliases = [ "/questions/43045" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [SMPP parse with lua](/questions/43045/smpp-parse-with-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43045-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43045-score" class="post-score" title="current number of votes">0</div><span id="post-43045-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! Sorry for my bad english!</p><p>I write lua script for parse smpp protocol do local smpp_packets = 0 local tcp_ack_time_count = 0 local tcp_ack_time_sum = 0 local submit_sm = 0 local submit_sm_resp = 0 local deliver_sm = 0 local deliver_sm_resp = 0 local mo_deliver_sm = 0</p><pre><code>local function init_listener()
    local tap = Listener.new(&quot;smpp&quot;)
    local ip_dst = Field.new(&quot;ip.dst&quot;)
    local ip_src = Field.new(&quot;ip.src&quot;)
    local frame_number = Field.new(&quot;frame.number&quot;)
    local frame_time = Field.new(&quot;frame.time&quot;)
    local frame_epochtime = Field.new(&quot;frame.time_epoch&quot;)
    local tcp_analysis_ack_rtt = Field.new(&quot;tcp.analysis.ack_rtt&quot;)
    local smpp_command_id = Field.new(&quot;smpp.command_id&quot;)
    local smpp_sequence_number = Field.new(&quot;smpp.sequence_number&quot;)
    local smpp_message_id = Field.new(&quot;smpp.message_id&quot;)
    local smpp_receipted_message_id = Field.new(&quot;smpp.receipted_message_id&quot;)
    local smpp_esm_submit_msg_type = Field.new(&quot;smpp.esm.submit.msg_type&quot;)
    local smpp = Field.new(&quot;smpp&quot;)

    function tap.packet(pinfo,tvb,ip)
        local src = tostring(ip_src())
        local dst = tostring(ip_dst())
        local frame = tostring(frame_number())
        local frametime = tostring(frame_time())
        local frameepoch = tostring(frame_epochtime())
        local command_id = smpp_command_id()
        local sequence_number = smpp_sequence_number()
        local message_id = smpp_message_id()
        local receipted_message_id = smpp_receipted_message_id()
        local esm_submit_msg_type = smpp_esm_submit_msg_type()
        local out_message_id = &quot;&quot;
        local out_receipted_message_id = &quot;&quot;
        local out_esm_submit_msg_type = &quot;&quot;
        --local _smpp = smpp()

        if message_id ~= nil then
            out_message_id = message_id
        end

        if receipted_message_id ~= nil then
            out_receipted_message_id = receipted_message_id
        end

        if esm_submit_msg_type ~= nil then
            out_esm_submit_msg_type = esm_submit_msg_type
        end

        print(string.format(&quot;%s|%s|%s|%s|%s|%s|%s&quot;, frame, frameepoch, command_id, sequence_number, out_message_id, out_receipted_message_id, out_esm_submit_msg_type))

    end
end
init_listener()</code></pre><p>end</p><p>if frame include more one smpp packet my script output this</p><pre><code>40495|1433778261.482167000|4|459182|||0
40495|1433778261.482167000|4|459182|||0
40495|1433778261.482167000|4|459182|||0
40495|1433778261.482167000|4|459182|||0
40495|1433778261.482167000|4|459182|||0
40495|1433778261.482167000|4|459182|||0
40495|1433778261.482167000|4|459182|||0
40495|1433778261.482167000|4|459182|||0
40495|1433778261.482167000|4|459182|||0</code></pre><p>459182 But packets in frame with sequence number 459182-459190</p><p>How i can take sequence number and another field for every smpp packet?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-smpp" rel="tag" title="see questions tagged &#39;smpp&#39;">smpp</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '15, 06:52</strong></p><img src="https://secure.gravatar.com/avatar/24ce4dbd85a337d5f7d5b63eba2ed2ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sergey%20%20Dergachev&#39;s gravatar image" /><p><span>Sergey Derg...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sergey  Dergachev has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Jun '15, 17:24</strong> </span></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span></p></div></div><div id="comments-container-43045" class="comments-container"></div><div id="comment-tools-43045" class="comment-tools"></div><div class="clear"></div><div id="comment-43045-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="43050"></span>

<div id="answer-container-43050" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43050-score" class="post-score" title="current number of votes">0</div><span id="post-43050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You'd have to put field selector in "{}" brackets and they will return a table</p><p>Then you iterate over a table something along the lines like below</p><pre><code>        local command_id_tbl = { smpp_command_id() } 
        local sequence_number_tbl = { smpp_sequence_number() }
        local message_id_tbl = { smpp_message_id() } 
        local receipted_message_id_tbl = { smpp_receipted_message_id() }
        local esm_submit_msg_type_tbl = { smpp_esm_submit_msg_type() }

        for i, sequence_number in ipairs(sequence_number_tbl)
        do
            print(string.format(&quot;%s|%s|%s|%s&quot;, frame, frameepoch, command_id_tbl[i], sequence_number_tbl[i]))

        end
</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '15, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p><span>izopizo</span><br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div></div><div id="comments-container-43050" class="comments-container"><span id="43051"></span><div id="comment-43051" class="comment"><div id="post-43051-score" class="comment-score"></div><div class="comment-text"><p>Thank you But don't work! If have packet with <a href="http://www.foto-me.ru/v.php?id=159acd47a8cebc47f256b2bbd7a58f61">link text</a></p><p>In table message_id only one element, but to which the packet is this element can not be determined</p></div><div id="comment-43051-info" class="comment-info"><span class="comment-age">(10 Jun '15, 08:00)</span> <span class="comment-user userinfo">Sergey Derg...</span></div></div></div><div id="comment-tools-43050" class="comment-tools"></div><div class="clear"></div><div id="comment-43050-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="43612"></span>

<div id="answer-container-43612" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43612-score" class="post-score" title="current number of votes">0</div><span id="post-43612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Since there could be multiple SMPP messages in a single captured frame (i.e., a single IP packet and TCP segment), and they might not each have a Message ID field, you'll have to keep track of each SMPP message as its parsed and which Message ID each has (if any).</p><p>See the answer for question #<a href="https://ask.wireshark.org/questions/43543/how-to-iterating-though-a-bundled-ss7-sctp-packet-in-lua">43543</a> for an idea of how to do that.</p><p>Basically the idea is to keep a Lua table indexed by the frame numbers, and the value of that frame number entry would be the number of Message ID fields already parsed/seen. Since your <code>tap.packet()</code> function will be invoked by Wireshark for each SMPP message, you can figure out how many (if any) Message ID fields have already been accounted for or if there's a new one.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '15, 17:35</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-43612" class="comments-container"></div><div id="comment-tools-43612" class="comment-tools"></div><div class="clear"></div><div id="comment-43612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

