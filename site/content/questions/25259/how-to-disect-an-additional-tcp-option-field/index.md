+++
type = "question"
title = "How to disect an additional TCP Option Field?"
description = '''Hi All, I am new to Dissectors in Lua. I have a very good idea on how to dissect an complete header but I am not sure how to go about dissecting a sub-field. For example if I have a TCP Option which is additional to the normal options (MSS,window scale,nop,timestamp,TCP SACK - not necessarily in tha...'''
date = "2013-09-26T00:16:00Z"
lastmod = "2013-09-29T17:43:00Z"
weight = 25259
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/25259" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to disect an additional TCP Option Field?](/questions/25259/how-to-disect-an-additional-tcp-option-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25259-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25259-score" class="post-score" title="current number of votes">0</div><span id="post-25259-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I am new to Dissectors in Lua. I have a very good idea on how to dissect an complete header but I am not sure how to go about dissecting a sub-field. For example if I have a TCP Option which is additional to the normal options (MSS,window scale,nop,timestamp,TCP SACK - not necessarily in that order) how will I parse the option? Do I have to dissect the Options Field from the beginning or is there anyway I can start parsing from the middle (ie after the default TCP Options -MSS,etc,.)? Any help would be really appreciated!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '13, 00:16</strong></p><img src="https://secure.gravatar.com/avatar/ad052d539b2a3dab9073e306f891eeb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vinay&#39;s gravatar image" /><p><span>Vinay</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vinay has no accepted answers">0%</span></p></div></div><div id="comments-container-25259" class="comments-container"></div><div id="comment-tools-25259" class="comment-tools"></div><div class="clear"></div><div id="comment-25259-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25295"></span>

<div id="answer-container-25295" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25295-score" class="post-score" title="current number of votes">1</div><span id="post-25295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Vinay has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As far as I can understand you are looking for a custom sub-dissecting of an existing protocol. Unfortunately, Lua does not support sub-dissection (I recently came to this website with a similar problem). Dissectors in Lua (e.g. post or chained dissection) can only be called instead of, or after an existing dissection protocol.</p><p>You might be looking for a chained dissection. (<a href="http://wiki.wireshark.org/Lua/Dissectors">Wiki Lua Dissectors</a>)</p><p>If I misunderstood your question, can you please clarify your problem?</p><p>Best regards, Gerald</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '13, 18:21</strong></p><img src="https://secure.gravatar.com/avatar/57b93085a535373e73bac2c71695ff0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald&#39;s gravatar image" /><p><span>Gerald</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald has one accepted answer">100%</span></p></div></div><div id="comments-container-25295" class="comments-container"><span id="25299"></span><div id="comment-25299" class="comment"><div id="post-25299-score" class="comment-score"></div><div class="comment-text"><p>Hi Gerald,</p><p>Thank you for the pointer! It cleared alot of things for me. I had one small followup. You have got my question right. So basically I have this packet which has the TCP Options as MSS,Window Scale,NOP,timestamp,TCP SACK, and unknown. This unknown section is what I am looking to parse. When I write the chained dissector do I need to start from the beginning (parse MSS, Window Scale, etc,.) and then finally reach unknown section or is there anyway I can jump directly to the unknown section?</p><p>Regards,</p><p>Vinay</p></div><div id="comment-25299-info" class="comment-info"><span class="comment-age">(26 Sep '13, 23:37)</span> <span class="comment-user userinfo">Vinay</span></div></div><span id="25347"></span><div id="comment-25347" class="comment"><div id="post-25347-score" class="comment-score"></div><div class="comment-text"><p>If you know the exact number of bytes you want to dissect (e.g. always byte 10-13) you can dissect only those bytes with your custom dissector.</p><p>Maybe you can also use 'Field.new()' to gather some information about an existing field previous to your custom field. I don't know if you can extract, for example, the byte position.</p><p>This will leave you with something like this:</p><pre><code>some_field_f   = Field.new(&quot;tcp.field&quot;)
tcp_proto      = Proto(&quot;customtcp&quot;,&quot;TCP Protocol&quot;)

-- (Chain-)Dissector function
function tcp_proto.dissector(buf,pinfo,tree)
   -- Call the tcp-dissector
   TCP_dissector:call(buf,pinfo,tree)
   pinfo.cols.protocol = &quot;Custom&quot;
   some_field = some_field_f()
   -- Extract information from some_field or
   -- Dissect buf(10,4) directly 
end

local dissector_table = DissectorTable.get(&quot;tcp.port&quot;)
TCP_dissector = dissector_table:get_dissector(port)
dissector_table:add(port, tcp_proto)</code></pre><p>Best regards, Gerald</p></div><div id="comment-25347-info" class="comment-info"><span class="comment-age">(29 Sep '13, 17:43)</span> <span class="comment-user userinfo">Gerald</span></div></div></div><div id="comment-tools-25295" class="comment-tools"></div><div class="clear"></div><div id="comment-25295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25312"></span>

<div id="answer-container-25312" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25312-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25312-score" class="post-score" title="current number of votes">0</div><span id="post-25312-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Why don't you update the existing protocol to fit with your custom protocol ? I had the same problem but I'm not using Lua dissector. For example I had custom field on RPL field of ipv6 protocol, I added my own code to parse them and now it work.</p><p>As I said I'm not using Lua so I'm probably totally wrong but at least I would have learned something.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '13, 05:21</strong></p><img src="https://secure.gravatar.com/avatar/4ec6105789137df01b9abed5fcb9ab95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Afrim&#39;s gravatar image" /><p><span>Afrim</span><br />
<span class="score" title="160 reputation points">160</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Afrim has 2 accepted answers">22%</span></p></div></div><div id="comments-container-25312" class="comments-container"></div><div id="comment-tools-25312" class="comment-tools"></div><div class="clear"></div><div id="comment-25312-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

