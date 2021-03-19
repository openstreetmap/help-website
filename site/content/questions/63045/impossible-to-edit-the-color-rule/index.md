+++
type = "question"
title = "Impossible to edit the color rule"
description = '''Hi everyone, I&#x27;m currently working on a dissector and I&#x27;d like to add my own color rule. It worked, but now, I&#x27;d like to change the foreground color that I&#x27;ve chosen. However, when I try to save with &quot;Ok&quot;, an error message pops up telling me: &quot;Your coloring rules file contains unknown rule. Wireshar...'''
date = "2017-07-24T07:17:00Z"
lastmod = "2017-10-25T11:32:00Z"
weight = 63045
keywords = [ "color", "dissector", "rule", "wireshark" ]
aliases = [ "/questions/63045" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Impossible to edit the color rule](/questions/63045/impossible-to-edit-the-color-rule)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63045-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63045-score" class="post-score" title="current number of votes">0</div><span id="post-63045-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>I'm currently working on a dissector and I'd like to add my own color rule. It worked, but now, I'd like to change the foreground color that I've chosen. However, when I try to save with "Ok", an error message pops up telling me: "Your coloring rules file contains unknown rule. Wireshark doesn't recognize one or more of you coloring rules. They have been disabled."</p><p>I don't understand why it doesn't work. Even if I open the rules and close them just by clicking "Ok", the same message pops up, even if there isn't any modification. I also tried to remove all the rules, the message still appears.</p><p>Do you have any idea?</p><p>Thanks in advance,</p><p>Matt</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-color" rel="tag" title="see questions tagged &#39;color&#39;">color</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-rule" rel="tag" title="see questions tagged &#39;rule&#39;">rule</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '17, 07:17</strong></p><img src="https://secure.gravatar.com/avatar/bd2aa9f8bc1b7271efcc67eab4613190?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MattJuillet&#39;s gravatar image" /><p><span>MattJuillet</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MattJuillet has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Jul '17, 07:18</strong> </span></p></div></div><div id="comments-container-63045" class="comments-container"></div><div id="comment-tools-63045" class="comment-tools"></div><div class="clear"></div><div id="comment-63045-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="63057"></span>

<div id="answer-container-63057" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63057-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63057-score" class="post-score" title="current number of votes">-1</div><span id="post-63057-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MattJuillet has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>My suggestion would be to navigate to your "Personal configuration" directory (<em>Help -&gt; About Wireshark -&gt; Folders -&gt; Personal configuration</em>) and rename your <code>colorfilters</code> file so that you can save a copy of it, e.g., <code>colorfilters_save</code>.</p><p>After that, navigate to the Wireshark installation directory and copy the default <code>colorfilters</code> file from there over to your "Personal configuration" directory, effectively replacing the old file.</p><p>At this point, you should be able to add your custom color filters either via Wireshark's GUI or by copying/pasting your custom entries from your saved file to the new file using any text editor.</p><p><strong>Note</strong>: You will likely need to perform these steps for all of your profiles in which a <code>colorfilters</code> file exists.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '17, 12:07</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-63057" class="comments-container"><span id="63058"></span><div id="comment-63058" class="comment"><div id="post-63058-score" class="comment-score">1</div><div class="comment-text"><p>Perfect, it works! I don't really understand what was the cause, but at least my issue is solved :).</p></div><div id="comment-63058-info" class="comment-info"><span class="comment-age">(24 Jul '17, 12:14)</span> <span class="comment-user userinfo">MattJuillet</span></div></div></div><div id="comment-tools-63057" class="comment-tools"></div><div class="clear"></div><div id="comment-63057-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="63046"></span>

<div id="answer-container-63046" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63046-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63046-score" class="post-score" title="current number of votes">1</div><span id="post-63046-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is likely to have been due to a change in the coloring rules, this question has been asked mutiple times before, e.g. <a href="https://ask.wireshark.org/questions/58300/your-coloring-rules-files-contains-unknown-rules">here</a>, <a href="https://ask.wireshark.org/questions/55840/coloring-rules-ok-button-grayed-out-after-update-to-wireshark-220">here</a> and <a href="https://ask.wireshark.org/questions/55504/getting-colorfilter-error-after-upgrading-to-220">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '17, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-63046" class="comments-container"><span id="63050"></span><div id="comment-63050" class="comment"><div id="post-63050-score" class="comment-score"></div><div class="comment-text"><p>Hi Grahamb,</p><p>I have consulted all these posts before sending my request and none of them seems to correspond to my issue: I don't have done any update recently, and I don't use any checksum (it doesn't work even if I remove all the rules). I think my problem is different.</p><p>Thank you for your help anyway!</p><p>Matt</p></div><div id="comment-63050-info" class="comment-info"><span class="comment-age">(24 Jul '17, 08:16)</span> <span class="comment-user userinfo">MattJuillet</span></div></div><span id="64200"></span><div id="comment-64200" class="comment"><div id="post-64200-score" class="comment-score">-1</div><div class="comment-text"><p>Had the EXACT same issue.</p><p>I found the issue 5 minutes ago on the first link grahamb posted.</p><p>Using the old legacy wireshark, I was able to delete the checksum coloring rules, which I was unable to do in the new client.</p><p>Thanks</p></div><div id="comment-64200-info" class="comment-info"><span class="comment-age">(25 Oct '17, 11:32)</span> <span class="comment-user userinfo">jerioux</span></div></div></div><div id="comment-tools-63046" class="comment-tools"></div><div class="clear"></div><div id="comment-63046-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

