+++
type = "question"
title = "Antenna Selection (ASEL) Capabilities in HT control field"
description = '''ASEL is an 802.11n MIMO technique which is cheaper to implement compared with beamforming. Details of the technique can be found here:  http://www.merl.com/publications/docs/TR2006-057.pdf I want to be able to see if units do indeed employ this feature.  ASEL capability is defined in the &quot;ASEL contr...'''
date = "2015-07-18T22:53:00Z"
lastmod = "2015-07-20T20:19:00Z"
weight = 44290
keywords = [ "display-filter" ]
aliases = [ "/questions/44290" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Antenna Selection (ASEL) Capabilities in HT control field](/questions/44290/antenna-selection-asel-capabilities-in-ht-control-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44290-score" class="post-score" title="current number of votes">0</div><span id="post-44290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>ASEL is an 802.11n MIMO technique which is cheaper to implement compared with beamforming. Details of the technique can be found here:</p><p><a href="http://www.merl.com/publications/docs/TR2006-057.pdf">http://www.merl.com/publications/docs/TR2006-057.pdf</a></p><p>I want to be able to see if units do indeed employ this feature.</p><p>ASEL capability is defined in the "ASEL control field" of the "HT control field" in the MAC header</p><p>The exact location of the frame is here: <a href="https://books.google.com/books?id=0GwFrd90G3kC&amp;pg=PA413&amp;lpg=PA413&amp;dq=asel+802.11+ht+control+field&amp;source=bl&amp;ots=0SPEGKQcUz&amp;sig=TNEWYeCGCQm617D4HfNijYQHiA4&amp;hl=en&amp;sa=X&amp;ved=0CDIQ6AEwA2oVChMIypvdibbmxgIVEFGICh0JkA4z#v=onepage&amp;q=asel%20802.11%20ht%20control%20field&amp;f=false">https://books.google.com/books?id=0GwFrd90G3kC&amp;pg=PA413&amp;lpg=PA413&amp;dq=asel+802.11+ht+control+field&amp;source=bl&amp;ots=0SPEGKQcUz&amp;sig=TNEWYeCGCQm617D4HfNijYQHiA4&amp;hl=en&amp;sa=X&amp;ved=0CDIQ6AEwA2oVChMIypvdibbmxgIVEFGICh0JkA4z#v=onepage&amp;q=asel%20802.11%20ht%20control%20field&amp;f=false</a></p><p>I have tried using the following filter using Wireshark with no success: wlan_mgt.asel.capable <a href="https://www.wireshark.org/docs/dfref/w/wlan_mgt.html">https://www.wireshark.org/docs/dfref/w/wlan_mgt.html</a></p><p>Can someone please explain to me what I'm doing wrong or how I can go about finding the correct way of filtering packets to find this field?</p><p>Many thanks in advance!</p><p>B</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jul '15, 22:53</strong></p><img src="https://secure.gravatar.com/avatar/626156d2cea2fb4e438d8eee96c8f621?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John%20Snow&#39;s gravatar image" /><p><span>John Snow</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John Snow has no accepted answers">0%</span></p></div></div><div id="comments-container-44290" class="comments-container"></div><div id="comment-tools-44290" class="comment-tools"></div><div class="clear"></div><div id="comment-44290-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="44316"></span>

<div id="answer-container-44316" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44316-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44316-score" class="post-score" title="current number of votes">0</div><span id="post-44316-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>wlan_mgt.asel.capable == 1</p><p>That field name is a boolean type. You must provide whether it exists (1) or does not exist (0).</p><p>Here is a tip for determining applicable values for field names in wireshark:</p><ol><li>In the Packet Details pane, find the value that you would like to filter</li><li>Right click on the field and select "Prepare a Filter" and then choose Selected</li><li>In the filter toolbar, you should see the desired filter. Then change the value accordingly</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jul '15, 17:30</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-44316" class="comments-container"></div><div id="comment-tools-44316" class="comment-tools"></div><div class="clear"></div><div id="comment-44316-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="44318"></span>

<div id="answer-container-44318" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44318-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44318-score" class="post-score" title="current number of votes">0</div><span id="post-44318-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In the HT Control field:</p><p>ASEL command: <code>wlan_mgt.htc.lac.asel.command</code></p><p>ASEL data: <code>wlan_mgt.htc.lac.asel.data</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jul '15, 20:19</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-44318" class="comments-container"></div><div id="comment-tools-44318" class="comment-tools"></div><div class="clear"></div><div id="comment-44318-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

