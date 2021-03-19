+++
type = "question"
title = "Related SMPP submit_sm filter"
description = '''Hello, everyone! I&#x27;d like to filter out SMPP submit_resp&#x27;s with а non-OK status. It&#x27;s quite simple: (smpp.command_id == 0x80000004) &amp;amp;&amp;amp; !(smpp.command_status == 0x00000000)  But how can I filter out related SMPP submit_sm&#x27;s without knowing of an absolute value of the SMPP sequence number? The...'''
date = "2015-07-14T01:01:00Z"
lastmod = "2015-07-15T11:47:00Z"
weight = 44122
keywords = [ "smpp_commands", "smpp", "tshark", "display-filter" ]
aliases = [ "/questions/44122" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Related SMPP submit\_sm filter](/questions/44122/related-smpp-submit_sm-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44122-score" class="post-score" title="current number of votes">0</div><span id="post-44122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, everyone! I'd like to filter out SMPP submit_resp's with а non-OK status. It's quite simple:</p><pre><code>(smpp.command_id == 0x80000004) &amp;&amp; !(smpp.command_status == 0x00000000)</code></pre><p>But how can I filter out related SMPP submit_sm's without knowing of an absolute value of the SMPP sequence number? The goal is to create non-interactive tshark filtered dump.</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-smpp_commands" rel="tag" title="see questions tagged &#39;smpp_commands&#39;">smpp_commands</span> <span class="post-tag tag-link-smpp" rel="tag" title="see questions tagged &#39;smpp&#39;">smpp</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '15, 01:01</strong></p><img src="https://secure.gravatar.com/avatar/757f09b44d22198faf9a42110c95e01c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rusyarr&#39;s gravatar image" /><p><span>rusyarr</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rusyarr has no accepted answers">0%</span></p></div></div><div id="comments-container-44122" class="comments-container"><span id="44125"></span><div id="comment-44125" class="comment"><div id="post-44125-score" class="comment-score"></div><div class="comment-text"><p>There must be a way to get a sequence number as a variable.</p></div><div id="comment-44125-info" class="comment-info"><span class="comment-age">(14 Jul '15, 01:44)</span> <span class="comment-user userinfo">rusyarr</span></div></div></div><div id="comment-tools-44122" class="comment-tools"></div><div class="clear"></div><div id="comment-44122-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44183"></span>

<div id="answer-container-44183" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44183-score" class="post-score" title="current number of votes">0</div><span id="post-44183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Bash helped me.</p><p>It looks like this:</p><pre><code>tshark -r $folder/$suff.pcap.gz -Y &quot;$(filter=&quot;&quot;;sn=&quot;&quot;;for sn in $(tshark -r $folder/$suff.pcap.gz -Y &quot;(smpp.command_id == 0x80000004) &amp;&amp; !(smpp.command_status == 0x00000000)&quot; -Tfields -e &quot;smpp.sequence_number&quot;);do filter=&quot;$filter || smpp.sequence_number == $sn&quot;;done;echo $filter|cut -c 4-)&quot; -w $folder/$host4dump.submit_failed.pcap</code></pre><p>For short:</p><ol><li>First I look for the SMPP submit_resp's with а non-OK status. I use filter <code>(smpp.command_id == 0x80000004) &amp;&amp; !(smpp.command_status == 0x00000000)</code> for this purposes. <code>-Tfields -e "smpp.sequence_number"</code> only extract sequence numbers from the found packets.</li><li>Secondly I use this numbers as a new filter.</li><li><code>-w $folder/$host4dump.submit_failed.pcap</code> outpust extracted to a new file.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '15, 11:47</strong></p><img src="https://secure.gravatar.com/avatar/757f09b44d22198faf9a42110c95e01c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rusyarr&#39;s gravatar image" /><p><span>rusyarr</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rusyarr has no accepted answers">0%</span></p></div></div><div id="comments-container-44183" class="comments-container"></div><div id="comment-tools-44183" class="comment-tools"></div><div class="clear"></div><div id="comment-44183-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

