+++
type = "question"
title = "Exporting packets with Wireshark version 1.10.0"
description = '''Why when I save an export I have filtered 140,000 packets out of 386,000 packets, when I have the save the displayed packets does it save the whole 386,000 instead of the 140,000? I think this might be a bug with version 1.10.0 Wireshark'''
date = "2013-07-23T16:18:00Z"
lastmod = "2013-07-24T07:15:00Z"
weight = 23306
keywords = [ "filter", "saveas", "save", "export" ]
aliases = [ "/questions/23306" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Exporting packets with Wireshark version 1.10.0](/questions/23306/exporting-packets-with-wireshark-version-1100)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23306-score" class="post-score" title="current number of votes">0</div><span id="post-23306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Why when I save an export I have filtered 140,000 packets out of 386,000 packets, when I have the save the displayed packets does it save the whole 386,000 instead of the 140,000? I think this might be a bug with version 1.10.0 Wireshark</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-saveas" rel="tag" title="see questions tagged &#39;saveas&#39;">saveas</span> <span class="post-tag tag-link-save" rel="tag" title="see questions tagged &#39;save&#39;">save</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jul '13, 16:18</strong></p><img src="https://secure.gravatar.com/avatar/328e4e3c363565d7a50d22167dd1a5b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="philvilla&#39;s gravatar image" /><p><span>philvilla</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="philvilla has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Jul '13, 18:09</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-23306" class="comments-container"></div><div id="comment-tools-23306" class="comment-tools"></div><div class="clear"></div><div id="comment-23306-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23307"></span>

<div id="answer-container-23307" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23307-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23307-score" class="post-score" title="current number of votes">1</div><span id="post-23307-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need to use the "Export Specified Packets" function in the file menu, not the "Save as" menu option. In the "Export Specified Packets" dialog you also need to make sure that in the "Packet Range" pane you selected "All Packets" and the "Displayed" column.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '13, 16:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-23307" class="comments-container"></div><div id="comment-tools-23307" class="comment-tools"></div><div class="clear"></div><div id="comment-23307-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23308"></span>

<div id="answer-container-23308" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23308-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23308-score" class="post-score" title="current number of votes">0</div><span id="post-23308-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As Jasper noted, in Wireshark 1.8 and later, "Save"/"Save As" and "Export Specified Packets" are two separate functions.</p><p>"Save"/"Save As", by design and intent, <em>saves</em>, i.e. writes out all the packets, including changes made to comments on the packets.</p><p>"Export Specified Packets" lets you write out some or all of the packets in the capture to a <em>different</em> file.</p><p>Were you trying to "save" - i.e., using "Save" or "Save As" - or were you trying to "export" - i.e., using "Export Specified Packets"? "Save"/"Save As" will, in Wireshark 1.8 and later, always write out all the packets; "Export Specified Packets" will let you select which packets to write out.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '13, 17:03</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23308" class="comments-container"><span id="23325"></span><div id="comment-23325" class="comment"><div id="post-23325-score" class="comment-score"></div><div class="comment-text"><p>I was trying to export which I said in the first post the application does not export only the selected packet it does all of them.</p></div><div id="comment-23325-info" class="comment-info"><span class="comment-age">(24 Jul '13, 07:15)</span> <span class="comment-user userinfo">philvilla</span></div></div></div><div id="comment-tools-23308" class="comment-tools"></div><div class="clear"></div><div id="comment-23308-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

