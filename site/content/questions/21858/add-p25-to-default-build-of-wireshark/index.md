+++
type = "question"
title = "add P25 to default build of Wireshark?"
description = '''Would it be possible for any of the developer people of the Macintosh OSX flavor of Wireshark to add the APCO P25 decoder to its default build in a future release in the near future? I&#x27;m not smart enough to do it. More information at op25.osmocom.org(slash)trac(slash)wiki.png(slash)wiki(slash)WireSh...'''
date = "2013-06-09T12:28:00Z"
lastmod = "2013-06-09T16:38:00Z"
weight = 21858
keywords = [ "p25", "add" ]
aliases = [ "/questions/21858" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [add P25 to default build of Wireshark?](/questions/21858/add-p25-to-default-build-of-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21858-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Would it be possible for any of the developer people of the Macintosh OSX flavor of Wireshark to add the APCO P25 decoder to its default build in a future release in the near future? I'm not smart enough to do it. More information at op25.osmocom.org(slash)trac(slash)wiki.png(slash)wiki(slash)WireSharkPage as to where to obtain the P25 source code. Thanx</p></div><div id="question-tags" class="tags-container tags">p25 add</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '13, 12:28</strong></p><img src="https://secure.gravatar.com/avatar/efb60f507a2b674d8c9215bdc7ba6ea6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="slacker2&#39;s gravatar image" /><p>slacker2<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="slacker2 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jun '13, 16:38</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-21858" class="comments-container"></div><div id="comment-tools-21858" class="comment-tools"></div><div class="clear"></div><div id="comment-21858-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21859"></span>

<div id="answer-container-21859" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21859-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, that is possible. But the best way to accomplish that is to ask the "APCO Project 25" people if they are fine with putting their patches in the official wireshark release. If they are fine with that, they can add the patches to an enhancement request at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and mark it as a patch.</p><p>Their code will then be evaluated and added to the Wireshark repository (assuming the code is good and does not conflict with other parts of Wireshark).</p><p>On a legal/moral note, we can not include code from others without their permission, so it is easiest if they offer their patches to us.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '13, 12:43</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21859" class="comments-container"><span id="21980"></span><div id="comment-21980" class="comment"><div id="post-21980-score" class="comment-score"></div><div class="comment-text"><p>The code is in the public domain and was released under the GNU General Public license. I don't know if you read any of the material posted at the URL that I cited in my original post (I had to put in "(slash)" for the actual slash character because this site's spaminator filter thought my post was spam if I included an http(colon) and/or (slash)es as part of what actually would be typed into the URL field).</p><p>Since the P25 decoder source code is posted online under the GNU General Public license on a website that tells you how to modify Wireshark to incorporate it (if you're lucky enough to be smart enough to modify Wireshark and compile the P25 decoder into it -- that ain't me), I'm thinking that the author is fine with it. Would the site maintainers here think otherwise?</p><p>I think I'll drop the developer/author of the P25 decoder a line. We do know who each other is. I'll just ask him to refer to this thread and would he please personally contribute his pubic domain source code to wherever it's gotta go for consideration to be included in future default distributions.</p></div><div id="comment-21980-info" class="comment-info"><span class="comment-age">(12 Jun '13, 14:03)</span> slacker2</div></div><span id="21994"></span><div id="comment-21994" class="comment"><div id="post-21994-score" class="comment-score"></div><div class="comment-text"><p>Osmocom guys already submitted some of their dissectors for inclusion in the Wireshark code. If they did not do it for the P25 dissector, there is probably a good reason and you should check with them why. I fully agree with SYN-bit's point of view.</p></div><div id="comment-21994-info" class="comment-info"><span class="comment-age">(13 Jun '13, 02:43)</span> Pascal Quantin</div></div></div><div id="comment-tools-21859" class="comment-tools"></div><div class="clear"></div><div id="comment-21859-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21860"></span>

<div id="answer-container-21860" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21860-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The default builds for <em>both</em> OSes for which we build binaries (Windows and OS X) build what's in the Wireshark source tree, so the way to get any particular dissector into the build is to get it into the Wireshark source tree, as per SYN-bit's comment.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '13, 16:38</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-21860" class="comments-container"></div><div id="comment-tools-21860" class="comment-tools"></div><div class="clear"></div><div id="comment-21860-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

