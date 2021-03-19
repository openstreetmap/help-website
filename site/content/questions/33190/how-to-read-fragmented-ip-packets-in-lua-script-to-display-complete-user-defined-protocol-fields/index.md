+++
type = "question"
title = "How to read fragmented IP packets in LUA script to display complete user defined protocol fields?"
description = '''I have a LUA script which will display user defined protocol fields on Wireshark, when the protocol filter is enabled and packet is not fragmented. When the packet is fragmented My user defined dissector would fail as the next segment is not processed. How to achieve this? Say when I highlight first...'''
date = "2014-05-30T02:22:00Z"
lastmod = "2014-06-04T23:33:00Z"
weight = 33190
keywords = [ "ipfragmentaion" ]
aliases = [ "/questions/33190" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to read fragmented IP packets in LUA script to display complete user defined protocol fields?](/questions/33190/how-to-read-fragmented-ip-packets-in-lua-script-to-display-complete-user-defined-protocol-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33190-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33190-score" class="post-score" title="current number of votes">0</div><span id="post-33190-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a LUA script which will display user defined protocol fields on Wireshark, when the protocol filter is enabled and packet is not fragmented.</p><p>When the packet is fragmented My user defined dissector would fail as the next segment is not processed.</p><p>How to achieve this? Say when I highlight first packet all the fragmented packets must be assembled and displayed? When ever the fragmented packet is highlighted, a notice saying check the first packet for full values?</p><p>How to achieve this, this is the task given to me in new company, please help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ipfragmentaion" rel="tag" title="see questions tagged &#39;ipfragmentaion&#39;">ipfragmentaion</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '14, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/bf6c503d201b5a1c5818150736c5405f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="testcoder&#39;s gravatar image" /><p><span>testcoder</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="testcoder has no accepted answers">0%</span></p></div></div><div id="comments-container-33190" class="comments-container"></div><div id="comment-tools-33190" class="comment-tools"></div><div class="clear"></div><div id="comment-33190-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="33418"></span>

<div id="answer-container-33418" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33418-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33418-score" class="post-score" title="current number of votes">0</div><span id="post-33418-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You have to assemble the different packets yourself. I created the following code in my dissector to assemble fragmented packages:</p><pre><code>function my_proto.dissector(buffer,pinfo,tree)
    local subtree = tree:add(my_proto, buffer(),&quot;My Packet&quot;)
    repeat
       if buffer:len() - len &gt;= 6 then
           len = len + 4 * packet_size
           if len &gt; buffer:len() then
               pinfo.desegment_len = len - buffer:len()
               return
           end
       else
           pinfo.desegment_len = DESEGMENT_ONE_MORE_SEGMENT
           return
       end
    until len &gt;= buffer:len()
    ---
    --- From here the normal protocol code
    subtree:add( .... )
     ...

end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '14, 23:13</strong></p><img src="https://secure.gravatar.com/avatar/cc22b4404576d307a99960c5bfc8a08f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bavh&#39;s gravatar image" /><p><span>bavh</span><br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bavh has one accepted answer">50%</span></p></div></div><div id="comments-container-33418" class="comments-container"></div><div id="comment-tools-33418" class="comment-tools"></div><div class="clear"></div><div id="comment-33418-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33419"></span>

<div id="answer-container-33419" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33419-score" class="post-score" title="current number of votes">0</div><span id="post-33419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How to achieve this?</p></blockquote><p>Turn on the "Reassemble fragmented IPv4 datagrams" preference for IPv4, or the "Reassemble fragmented IPv6 datagrams" for IPv6, so that Wireshark will reassemble fragmented IP packets for you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '14, 23:33</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-33419" class="comments-container"></div><div id="comment-tools-33419" class="comment-tools"></div><div class="clear"></div><div id="comment-33419-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

