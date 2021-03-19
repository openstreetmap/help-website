+++
type = "question"
title = "When changing profiles from the status bar i get an error, Any Solution ?"
description = '''When I attempt to change profiles via the status bar i get the following error.   This does seem to cause any major issues, i just click ok and the profile changes is just very annoying. I have tried uninstalling and reinstalling. This started to occur either when i put on 2.2.7 or went to win10 ent...'''
date = "2017-06-17T10:09:00Z"
lastmod = "2017-06-18T05:18:00Z"
weight = 62075
keywords = [ "status", "bar", "profiles" ]
aliases = [ "/questions/62075" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [When changing profiles from the status bar i get an error, Any Solution ?](/questions/62075/when-changing-profiles-from-the-status-bar-i-get-an-error-any-solution)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62075-score" class="post-score" title="current number of votes">0</div><span id="post-62075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I attempt to change profiles via the status bar i get the following error.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/2017-06-17_13_04_52-Clipboard_sruBfRG.png" alt="alt text" /></p><p>This does seem to cause any major issues, i just click ok and the profile changes is just very annoying. I have tried uninstalling and reinstalling. This started to occur either when i put on 2.2.7 or went to win10 enterprise on my system. They were both done near the same time. Has anyone ever saw this and is there a resolution?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-status" rel="tag" title="see questions tagged &#39;status&#39;">status</span> <span class="post-tag tag-link-bar" rel="tag" title="see questions tagged &#39;bar&#39;">bar</span> <span class="post-tag tag-link-profiles" rel="tag" title="see questions tagged &#39;profiles&#39;">profiles</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '17, 10:09</strong></p><img src="https://secure.gravatar.com/avatar/8e19bba7e40a62154983610c3a42edd1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mnmoose&#39;s gravatar image" /><p><span>mnmoose</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mnmoose has no accepted answers">0%</span></p></img></div></div><div id="comments-container-62075" class="comments-container"><span id="62078"></span><div id="comment-62078" class="comment"><div id="post-62078-score" class="comment-score"></div><div class="comment-text"><p>to clarify, did you mean "does <strong>not</strong> seem to cause any major issues" maybe? So there's a warning that's annoying because you have to click it away and it works without restart?</p></div><div id="comment-62078-info" class="comment-info"><span class="comment-age">(17 Jun '17, 12:11)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="62087"></span><div id="comment-62087" class="comment"><div id="post-62087-score" class="comment-score"></div><div class="comment-text"><p>that's correct it's just a pop up i receive. it's just a very annoying issue.</p></div><div id="comment-62087-info" class="comment-info"><span class="comment-age">(17 Jun '17, 13:35)</span> <span class="comment-user userinfo">mnmoose</span></div></div><span id="62092"></span><div id="comment-62092" class="comment"><div id="post-62092-score" class="comment-score"></div><div class="comment-text"><p>Yes, it's annoying. It's an undesirable consequence of the use of some libraries that add specific functionality to Wireshark, which do not support reconfiguration after a settings change. Switching profiles may cause this settings change, hence the warning. Fatal? No, but you have to be aware of the fact that certain functionality may act differently from the way it's currently configured. That's something easily overlooked, causing a lot of head scratching. Couldn't the libraries be replaced with better ones, that allow reconfiguration? We'd love to, but these aren't available right now.</p></div><div id="comment-62092-info" class="comment-info"><span class="comment-age">(18 Jun '17, 01:41)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-62075" class="comment-tools"></div><div class="clear"></div><div id="comment-62075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62089"></span>

<div id="answer-container-62089" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62089-score" class="post-score" title="current number of votes">0</div><span id="post-62089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mnmoose has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This warning pops up when changing/modifying SMI (MIB and PIB) paths or modules (Preferences -&gt; Name Resolution).</p><p>A possible workaround could be to remove your SMI paths or modules in your profiles (where it's not needed).</p><p>Side note: Every profile can have its own setting for SMI path/modules.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '17, 00:18</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p><span>Uli</span><br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-62089" class="comments-container"><span id="62099"></span><div id="comment-62099" class="comment"><div id="post-62099-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the information. Not sure why i just started to get this error since these profiles have always had enable OID resolution checked. Maybe it has something to do with windows 10 enterprise which i have just recently went to.</p></div><div id="comment-62099-info" class="comment-info"><span class="comment-age">(18 Jun '17, 05:18)</span> <span class="comment-user userinfo">mnmoose</span></div></div></div><div id="comment-tools-62089" class="comment-tools"></div><div class="clear"></div><div id="comment-62089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

