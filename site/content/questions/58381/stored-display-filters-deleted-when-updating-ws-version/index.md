+++
type = "question"
title = "Stored Display filters deleted when updating WS Version"
description = '''I have spent a lot of time creating display filters to use in many environments. When updating to 2.2.2 all the 30-40 display filters are now gone! Anyone know where they are stored and are we able to back them up before doing an update? Very costly to lose all of my work.'''
date = "2016-12-27T13:58:00Z"
lastmod = "2016-12-27T16:26:00Z"
weight = 58381
keywords = [ "deleted", "display", "filters", "missing" ]
aliases = [ "/questions/58381" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Stored Display filters deleted when updating WS Version](/questions/58381/stored-display-filters-deleted-when-updating-ws-version)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58381-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have spent a lot of time creating display filters to use in many environments. When updating to 2.2.2 all the 30-40 display filters are now gone! Anyone know where they are stored and are we able to back them up before doing an update? Very costly to lose all of my work.</p></div><div id="question-tags" class="tags-container tags">deleted display filters missing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Dec '16, 13:58</strong></p><img src="https://secure.gravatar.com/avatar/a2c36e0535e33d86a1738e74e85101fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="drewcrewof2&#39;s gravatar image" /><p>drewcrewof2<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="drewcrewof2 has no accepted answers">0%</span></p></div></div><div id="comments-container-58381" class="comments-container"></div><div id="comment-tools-58381" class="comment-tools"></div><div class="clear"></div><div id="comment-58381-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58382"></span>

<div id="answer-container-58382" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58382-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What's your OS?</p><p>Display filters are in a file named dfilters that will usually be in your "Personal Configuration" directory. You can find the location of that directory from the Wireshark -&gt; Help -&gt; About dialog, on the Folders tab.</p><p>Normally that directory is not touched on an upgrade.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '16, 16:26</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-58382" class="comments-container"><span id="58399"></span><div id="comment-58399" class="comment"><div id="post-58399-score" class="comment-score"></div><div class="comment-text"><p>Is Win 7 Ultimate. Thanks for the tip, I have hours invested. The removal has happened on 2 dev systems now.</p></div><div id="comment-58399-info" class="comment-info"><span class="comment-age">(28 Dec '16, 05:30)</span> drewcrewof2</div></div><span id="58403"></span><div id="comment-58403" class="comment"><div id="post-58403-score" class="comment-score"></div><div class="comment-text"><p>Answering my own question after investigating further. The drop down Display Filters are indeed in ( my system) <code>C:\Users\DrewCrewOf2\AppData\Roaming\Wireshark\recent_common\</code></p><p>However in the latest file there it has be set to all "NUL" (zeros) 13K of them! So is now gone! I went to a Acronis backup done days before the update to WS 2.2.2 and it still has my 13 K of Display filters. Some shown here below, so something killed the recent_common file contents during update::</p><pre><code>######## Recent display filters (latest last), cannot be altered through command line ########

recent.display_filter: skinny &amp;&amp; !skinny.messageId == 192  &amp;&amp; !skinny.messageId == 0 &amp;&amp; !skinny.messageId == 0x00000100 &amp;&amp; !skinny.messageId == 289 &amp;&amp; !skinny.messageId == 148 &amp;&amp; !skinny.messageId == 13 &amp;&amp; !skinny.messageId == 277 &amp;&amp; !skinny.messageId == 274 &amp;&amp; !skinny.messageId == 288 &amp;&amp; !skinny.messageId ==134 &amp;&amp; !skinny.messageId == 35 &amp;&amp; !skinny.messageId == 263
recent.display_filter: skinny &amp;&amp; !skinny.messageId == 192  &amp;&amp; !skinny.messageId == 0 &amp;&amp; !skinny.messageId ==0x00000100 &amp;&amp; !skinny.messageId == 289 &amp;&amp; !skinny.messageId == 148 &amp;&amp; !skinny.messageId ==13 &amp;&amp; !skinny.messageId == 277 &amp;&amp; !skinny.messageId == 274 &amp;&amp; !skinny.messageId == 288 &amp;&amp; !skinny.messageId == 134
recent.display_filter: skinny &amp;&amp; !skinny.messageId ==192  &amp;&amp; !skinny.messageId == 0 &amp;&amp; !skinny.messageId ==0x00000100 &amp;&amp; !skinny.messageId ==289 &amp;&amp; !skinny.messageId ==148 &amp;&amp; !skinny.messageId ==13 &amp;&amp; !skinny.messageId ==277 &amp;&amp; !skinny.messageId ==274 &amp;&amp; !skinny.messageId ==288 &amp;&amp; !skinny.messageId ==134
recent.display_filter: skinny &amp;&amp; !skinny.messageId ==192  &amp;&amp; !skinny.messageId == 0 &amp;&amp; !skinny.messageId ==0x00000100 &amp;&amp; !skinny.messageId ==289 &amp;&amp; !skinny.messageId ==148 &amp;&amp; !skinny.messageId ==13 &amp;&amp; !skinny.messageId ==277 &amp;&amp; !skinny.messageId ==274 &amp;&amp; !skinny.messageId ==288
recent.display_filter: skinny &amp;&amp; !skinny.messageId ==192  &amp;&amp; !skinny.messageId == 0 &amp;&amp; !skinny.messageId ==0x00000100 &amp;&amp; !skinny.messageId ==289 &amp;&amp; !skinny.messageId ==148 &amp;&amp; !skinny.messageId ==13 &amp;&amp; !skinny.messageId ==277 &amp;&amp; !skinny.messageId ==274
recent.display_filter: skinny &amp;&amp; !skinny.messageId ==192  &amp;&amp; !skinny.messageId == 0 &amp;&amp; !skinny.messageId ==0x00000100 &amp;&amp; !skinny.messageId ==289 &amp;&amp; !skinny.messageId ==148 &amp;&amp; !skinny.messageId ==13 &amp;&amp; !skinny.messageId ==277
recent.display_filter: skinny &amp;&amp; !skinny.messageId ==192  &amp;&amp; !skinny.messageId == 0 &amp;&amp; !skinny.messageId ==0x00000100 &amp;&amp; !skinny.messageId ==289 &amp;&amp; !skinny.messageId ==148 &amp;&amp; !skinny.messageId ==13</code></pre></div><div id="comment-58403-info" class="comment-info"><span class="comment-age">(28 Dec '16, 06:05)</span> drewcrewof2</div></div><span id="58404"></span><div id="comment-58404" class="comment"><div id="post-58404-score" class="comment-score"></div><div class="comment-text"><p>You have indicated that you found your display filters are in the file recent_common, this is not the list of saved display filters, this is the list of recently used display filters and is automatically overwritten on the exit of Wireshark.</p><p>The normal place to save display filters is in the dfilters file, using the dialog opened by Analyze -&gt; Display Filters, where each display filter can also be named.</p><p>I can't see anything in the source or installer that would wipe out recent_common and a test update from 2.3.0 something to the latest master didn't remove my recent_common entries.</p><p>What version are you upgrading from?</p></div><div id="comment-58404-info" class="comment-info"><span class="comment-age">(28 Dec '16, 07:46)</span> grahamb ♦</div></div></div><div id="comment-tools-58382" class="comment-tools"></div><div class="clear"></div><div id="comment-58382-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

