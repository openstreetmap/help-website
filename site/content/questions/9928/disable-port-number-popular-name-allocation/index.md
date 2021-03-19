+++
type = "question"
title = "Disable port number popular name allocation"
description = '''Hello all, Can anyone tell me how to stop wireshark giving the port numbers for TCP packets popular names like &quot;ddi-tcp&quot; and &quot;blackjack&quot; etc, I just want to see the port number. Regards Baz'''
date = "2012-04-04T08:02:00Z"
lastmod = "2012-04-04T08:04:00Z"
weight = 9928
keywords = [ "popular", "allocation", "disable", "port", "name" ]
aliases = [ "/questions/9928" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Disable port number popular name allocation](/questions/9928/disable-port-number-popular-name-allocation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9928-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>Can anyone tell me how to stop wireshark giving the port numbers for TCP packets popular names like "ddi-tcp" and "blackjack" etc, I just want to see the port number.</p><p>Regards</p><p>Baz</p></div><div id="question-tags" class="tags-container tags">popular allocation disable port name</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '12, 08:02</strong></p><img src="https://secure.gravatar.com/avatar/8fbeff627fe9082da131384ae21a5d85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baz&#39;s gravatar image" /><p>Baz<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baz has no accepted answers">0%</span></p></div></div><div id="comments-container-9928" class="comments-container"></div><div id="comment-tools-9928" class="comment-tools"></div><div class="clear"></div><div id="comment-9928-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9929"></span>

<div id="answer-container-9929" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9929-score" class="post-score" title="current number of votes">5</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sure, just disable "Name Resolution" for the "Transport Layer" in the View menu (for temporary effect), or go into the preferences and disabled it in the Name Resolutions section.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '12, 08:04</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-9929" class="comments-container"><span id="9931"></span><div id="comment-9931" class="comment"><div id="post-9931-score" class="comment-score"></div><div class="comment-text"><p>Thanks for that Jasper,</p><p>Can I use this method on pre captured files which I load back in to view?</p><p>Regards</p><p>Barr</p></div><div id="comment-9931-info" class="comment-info"><span class="comment-age">(04 Apr '12, 08:09)</span> Baz</div></div><span id="9932"></span><div id="comment-9932" class="comment"><div id="post-9932-score" class="comment-score"></div><div class="comment-text"><p>No need to worry,</p><p>I've just fingered it out. If you change the "View" setting you have to re-load the file.</p><p>Thanks</p><p>Baz</p></div><div id="comment-9932-info" class="comment-info"><span class="comment-age">(04 Apr '12, 08:13)</span> Baz</div></div><span id="9935"></span><div id="comment-9935" class="comment"><div id="post-9935-score" class="comment-score"></div><div class="comment-text"><p>If changing the "View" setting doesn't change what you see <em>without</em> having to reload the file, that's a bug (even if it's complicated to fix); please file a bug about that at <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>.</p></div><div id="comment-9935-info" class="comment-info"><span class="comment-age">(04 Apr '12, 08:32)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-9929" class="comment-tools"></div><div class="clear"></div><div id="comment-9929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

