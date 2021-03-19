+++
type = "question"
title = "Lldp Dissector Column Info"
description = '''Current Lldp Dissector column information just shows the &quot;System Description&quot; information. In the Profinet applications, this information does not help too much. On the other hand Chassis Id and Port Id gives much more information.  In the source code (packet-lldp.c), it is very easy to comment foll...'''
date = "2015-10-27T00:05:00Z"
lastmod = "2015-10-27T06:36:00Z"
weight = 46967
keywords = [ "lldp", "col_info", "columns" ]
aliases = [ "/questions/46967" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Lldp Dissector Column Info](/questions/46967/lldp-dissector-column-info)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46967-score" class="post-score" title="current number of votes">0</div><span id="post-46967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Current Lldp Dissector column information just shows the "System Description" information.</p><p>In the Profinet applications, this information does not help too much. On the other hand Chassis Id and Port Id gives much more information.</p><p>In the source code (packet-lldp.c), it is very easy to comment followig line:</p><pre><code>col_append_fstr(pinfo-&gt;cinfo, COL_INFO, &quot;System Name = %s &quot;, strPtr);</code></pre><p>And instead of this line, adding following to dissect_lldp_chassis_id function:</p><pre><code>col_append_fstr(pinfo-&gt;cinfo, COL_INFO, &quot;Chassis ID = %s &quot;, strPtr);</code></pre><p>But this change will affect whole Lldp messages' column information. I want to ask if I have a right to change it in this manner or not before I begin to implementation.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lldp" rel="tag" title="see questions tagged &#39;lldp&#39;">lldp</span> <span class="post-tag tag-link-col_info" rel="tag" title="see questions tagged &#39;col_info&#39;">col_info</span> <span class="post-tag tag-link-columns" rel="tag" title="see questions tagged &#39;columns&#39;">columns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '15, 00:05</strong></p><img src="https://secure.gravatar.com/avatar/6257a856e7271c04dd39469c7a5332ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BirolCapa&#39;s gravatar image" /><p><span>BirolCapa</span><br />
<span class="score" title="30 reputation points">30</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BirolCapa has no accepted answers">0%</span></p></div></div><div id="comments-container-46967" class="comments-container"></div><div id="comment-tools-46967" class="comment-tools"></div><div class="clear"></div><div id="comment-46967-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46969"></span>

<div id="answer-container-46969" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46969-score" class="post-score" title="current number of votes">0</div><span id="post-46969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I want to ask if I have a right to change it in this manner or not before I begin to implementation.</p></blockquote><p>Wireshark is an open <strong>source project licensed under the GPL</strong>. So, you have the all rights to change the source code based on what the GPL 'allows'. This translates to: yes, of course you can change that, as long as you adhere to the GPL.</p><p>If you want to submit your changes back to the Wireshark code base, it will most certainly depend on other criteria if the submission will be accepted (code quality, useful enhancements, etc.), than just that single modification to the Info column.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '15, 01:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-46969" class="comments-container"><span id="46970"></span><div id="comment-46970" class="comment"><div id="post-46970-score" class="comment-score"></div><div class="comment-text"><p>Hello Kurt, thank you for your answer.</p><p>I understand you. But I just don't understand if there is a rule or standard that community obeys about column information: For example, why did community choose system name instead of another field? Is there a rule or standard etc. Or it was a just decision of the developer of the lldp dissector?</p></div><div id="comment-46970-info" class="comment-info"><span class="comment-age">(27 Oct '15, 01:33)</span> <span class="comment-user userinfo">BirolCapa</span></div></div><span id="46974"></span><div id="comment-46974" class="comment"><div id="post-46974-score" class="comment-score">1</div><div class="comment-text"><p>As far as I know, there is no 'community' decison about these things. I'd say it's the decision of the developer.</p></div><div id="comment-46974-info" class="comment-info"><span class="comment-age">(27 Oct '15, 02:16)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-46969" class="comment-tools"></div><div class="clear"></div><div id="comment-46969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46981"></span>

<div id="answer-container-46981" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46981-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46981-score" class="post-score" title="current number of votes">0</div><span id="post-46981-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As Kurt described, based on the GPL you have the right to make the changes and redistributed them, including (offering of) source code.</p><p>What I won't see happening is this change being accepted into the main repository. This will not happen because the statement you quoted is part op <code>dissect_lldp_system_name()</code>, which is specifically written to "<code>/ Dissect System Name and description TLV /</code>", so this is executed when those TLVs are dissected.</p><p>What you seem to be missing is that <code>dissect_lldp_chassis_id()</code> is <strong>not</strong> adding to the info column. If you were to propose such change that might have a chance.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '15, 05:01</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-46981" class="comments-container"><span id="46982"></span><div id="comment-46982" class="comment"><div id="post-46982-score" class="comment-score"></div><div class="comment-text"><p>Hello Jaap, thank you for your answer,</p><p>To show Chassis id and Port id, I will comment following (at dissect_lldp_system_name)</p><p>"col_append_fstr(pinfo-&gt;cinfo, COL_INFO, "System Name = %s ", strPtr);" "col_append_fstr(pinfo-&gt;cinfo, COL_INFO, "System Description = %s ", strPtr);"</p><p>So column info will not show the System Name and description anymore, and I will add dissect_lldp_chassis_id to this:</p><p>"col_append_fstr(pinfo-&gt;cinfo, COL_INFO, "Chassis ID = %s ", strPtr);"</p><p>and I will add dissect_lldp_port_id to this:</p><p>"col_append_fstr(pinfo-&gt;cinfo, COL_INFO, "Port ID = %s ", strPtr);"</p><p>So whole LLDP will show Chassis Id and Port Id instead of System Name and Description.</p><p>This change will be very useful for Profinet, on the other hand I am not sure if it is appropriate for other users. That's why I am asking if there is a community decision about column info.</p></div><div id="comment-46982-info" class="comment-info"><span class="comment-age">(27 Oct '15, 05:12)</span> <span class="comment-user userinfo">BirolCapa</span></div></div><span id="46986"></span><div id="comment-46986" class="comment"><div id="post-46986-score" class="comment-score"></div><div class="comment-text"><p>So there seems to be a difference in opinion about what is useful to represent in the INFO column when dissecting LLDP, either within profinet, or other contexts.</p><p>In that case a dissector preference would allow the <strong>user</strong> to choose what his/her preference is, whereby the default preference would match the current behaviour.</p></div><div id="comment-46986-info" class="comment-info"><span class="comment-age">(27 Oct '15, 06:36)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-46981" class="comment-tools"></div><div class="clear"></div><div id="comment-46981-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

