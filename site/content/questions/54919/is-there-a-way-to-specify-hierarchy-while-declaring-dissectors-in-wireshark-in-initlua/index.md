+++
type = "question"
title = "Is there a way to specify hierarchy while declaring dissectors in wireshark in init.lua?"
description = '''Hi,  I am creating several dissectors for Wireshark in Lua. Basically I have several different protocols for which the dissectors need to be created. The issue is that some of these protocols use the same port numbers. So I wanted to know if there is a way to specify a hierarchy that should be follo...'''
date = "2016-08-17T06:26:00Z"
lastmod = "2016-08-17T06:26:00Z"
weight = 54919
keywords = [ "hierarchy", "lua", "dissector", "wireshark" ]
aliases = [ "/questions/54919" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a way to specify hierarchy while declaring dissectors in wireshark in init.lua?](/questions/54919/is-there-a-way-to-specify-hierarchy-while-declaring-dissectors-in-wireshark-in-initlua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54919-score" class="post-score" title="current number of votes">0</div><span id="post-54919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am creating several dissectors for Wireshark in Lua. Basically I have several different protocols for which the dissectors need to be created. The issue is that some of these protocols use the same port numbers. So I wanted to know if there is a way to specify a hierarchy that should be followed when dissecting the packets. For example if I have dissector_1 and dissector_2, and I have a packet whose source port falls in the range of dissector_1 and destination port falls in the range of dissector_2, then how can I force the packet to be dissected using dissector_1, as over here the dissector_1 is higher in the hierarchy. Edit: I have also noticed that if I create a dissector that analyses the port numbers and then based upon certain if-else conditions calls other dissectors it works fine, but if in this dissector I try and add preferences to specify the port numbers for dissector_1 then the dissector stops working altogether.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hierarchy" rel="tag" title="see questions tagged &#39;hierarchy&#39;">hierarchy</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Aug '16, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/3aaad26a48e6f507d8f9137404269a46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shobhit_garg91&#39;s gravatar image" /><p><span>shobhit_garg91</span><br />
<span class="score" title="16 reputation points">16</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shobhit_garg91 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Aug '16, 13:28</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-54919" class="comments-container"></div><div id="comment-tools-54919" class="comment-tools"></div><div class="clear"></div><div id="comment-54919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

