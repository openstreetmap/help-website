+++
type = "question"
title = "SMPP commands,tree  with filter"
description = '''there is a way to aply a filter in a command like this:  tshark -nr input.pcap -q -z smpp_commands,tree  I have a pcap file with several IPs and I want to make a filter with ip.src==x.x.x.x and then show the smpp_commands,tree. thanks and regards'''
date = "2013-06-22T16:37:00Z"
lastmod = "2013-07-15T13:43:00Z"
weight = 22248
keywords = [ "filter", "smpp", "tree", "smpp_commands" ]
aliases = [ "/questions/22248" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [SMPP commands,tree with filter](/questions/22248/smpp-commandstree-with-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22248-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22248-score" class="post-score" title="current number of votes">0</div><span id="post-22248-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>there is a way to aply a filter in a command like this: tshark -nr input.pcap -q -z smpp_commands,tree</p><p>I have a pcap file with several IPs and I want to make a filter with ip.src==x.x.x.x and then show the smpp_commands,tree.</p><p>thanks and regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-smpp" rel="tag" title="see questions tagged &#39;smpp&#39;">smpp</span> <span class="post-tag tag-link-tree" rel="tag" title="see questions tagged &#39;tree&#39;">tree</span> <span class="post-tag tag-link-smpp_commands" rel="tag" title="see questions tagged &#39;smpp_commands&#39;">smpp_commands</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '13, 16:37</strong></p><img src="https://secure.gravatar.com/avatar/ca20bac738bbb8b012045602a77d7115?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fachav2&#39;s gravatar image" /><p><span>fachav2</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fachav2 has no accepted answers">0%</span></p></div></div><div id="comments-container-22248" class="comments-container"></div><div id="comment-tools-22248" class="comment-tools"></div><div class="clear"></div><div id="comment-22248-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22977"></span>

<div id="answer-container-22977" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22977-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22977-score" class="post-score" title="current number of votes">1</div><span id="post-22977-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="fachav2 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I did manage to work this out with:</p><pre><code>$ tshark -nr FILENAME -R&quot;ip.addr==IPADDR&quot; -2 -qz smpp_commands,tree
===================================================================
 SM_PP Operations             value         rate         percent
-------------------------------------------------------------------
 SMPP Operations               411       0.001066                
  SMPP Requests                  99       0.000257          24.09%
   Enquire_link                   14       0.000036          14.14%
   Submit_sm                      85       0.000220          85.86%
  SMPP Responses                312       0.000809          75.91%
   Deliver_sm - resp             282       0.000731          90.38%
   Enquire_link - resp            28       0.000073           8.97%
   Submit_sm - resp                2       0.000005           0.64%
 SMPP Response Status         312       0.000809                
  Ok                           312       0.000809         100.00%

===================================================================</code></pre><p>And if I remove the filter -R "" -2 I will get all the traffic. I have the following wireshark/tshark:</p><pre><code>TShark 1.10.0 (SVN Rev 49790 from /trunk-1.10)</code></pre><p><strong>NOTE</strong>: That if you specify ip.src you will see only the SMPP commands generated from that IP and not responses or commands generated from the destination IP. Sometimes this is handy because you can see (even count) if all your command have responses and vice-versa.</p><p>More information you can find from tshark help page: <a href="http://www.wireshark.org/docs/man-pages/tshark.html">http://www.wireshark.org/docs/man-pages/tshark.html</a></p><p>And last but not least HAPPY BIRTHDAY TO <a href="https://blog.wireshark.org/2013/07/fifteen-years/?utm_source=rss&amp;utm_medium=rss&amp;utm_campaign=fifteen-years">WIRESHARK</a> :).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '13, 12:02</strong></p><img src="https://secure.gravatar.com/avatar/57dca282828fcb7b6086c0a77af93ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Edmond&#39;s gravatar image" /><p><span>Edmond</span><br />
<span class="score" title="181 reputation points">181</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Edmond has 2 accepted answers">33%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jul '13, 14:44</strong> </span></p></div></div><div id="comments-container-22977" class="comments-container"><span id="22978"></span><div id="comment-22978" class="comment"><div id="post-22978-score" class="comment-score"></div><div class="comment-text"><p>multiple passes (-2) that was the option i needed. Yes I have to upgrade my tshark. I will try and let you know about</p></div><div id="comment-22978-info" class="comment-info"><span class="comment-age">(15 Jul '13, 13:43)</span> <span class="comment-user userinfo">fachav2</span></div></div></div><div id="comment-tools-22977" class="comment-tools"></div><div class="clear"></div><div id="comment-22977-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22249"></span>

<div id="answer-container-22249" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22249-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22249-score" class="post-score" title="current number of votes">0</div><span id="post-22249-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try this</p><p>tshark -nr &lt;pcapfile&gt; -Y "ip.src==x.x.x.x" -qz smpp_commands,tree</p><p>If it is not taking -Y then try giving -R.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '13, 17:01</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Jun '13, 17:06</strong> </span></p></div></div><div id="comments-container-22249" class="comments-container"><span id="22974"></span><div id="comment-22974" class="comment"><div id="post-22974-score" class="comment-score"></div><div class="comment-text"><p>thanks but it did not work. The -Y option crash, but the -R is accepted, but no matter what IP I filter with -R opt. the result is always the same.</p><p>Any one know any thing about this?</p></div><div id="comment-22974-info" class="comment-info"><span class="comment-age">(15 Jul '13, 08:37)</span> <span class="comment-user userinfo">fachav2</span></div></div></div><div id="comment-tools-22249" class="comment-tools"></div><div class="clear"></div><div id="comment-22249-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

