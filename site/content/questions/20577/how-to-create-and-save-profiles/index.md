+++
type = "question"
title = "How to create and save profiles?"
description = '''I can&#x27;t figure out how to create and save a profile. I&#x27;m using Version 1.6.11 (SVN Rev 45257 from /trunk-1.6) on Windows 7. If I open the Edit:Configuration Profiles menu item the only options are New, Copy, Delete, OK, Apply, and Cancel (no Save button). If I select any of the existing profiles my ...'''
date = "2013-04-18T08:32:00Z"
lastmod = "2013-04-18T10:26:00Z"
weight = 20577
keywords = [ "profile" ]
aliases = [ "/questions/20577" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to create and save profiles?](/questions/20577/how-to-create-and-save-profiles)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20577-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I can't figure out how to create and save a profile. I'm using Version 1.6.11 (SVN Rev 45257 from /trunk-1.6) on Windows 7. If I open the Edit:Configuration Profiles menu item the only options are New, Copy, Delete, OK, Apply, and Cancel (no Save button). If I select any of the existing profiles my current preferences (what I'm trying to save) get replaced with ones from the profile I load. New seems to set everything back to defaults.</p><p>I'm specifically trying to save a default Capture Filter, display column configuration, and Time display format.</p></div><div id="question-tags" class="tags-container tags">profile</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '13, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/f00433cd3f4d686395b091a36b834a1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gismo&#39;s gravatar image" /><p>gismo<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gismo has no accepted answers">0%</span></p></div></div><div id="comments-container-20577" class="comments-container"></div><div id="comment-tools-20577" class="comment-tools"></div><div class="clear"></div><div id="comment-20577-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20584"></span>

<div id="answer-container-20584" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20584-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>See the Wireshark User's Guide:<br />
<a href="http://www.wireshark.org/docs/wsug_html_chunked/ChCustConfigProfilesSection.html">Configuration Profiles</a><br />
or<br />
read my article about <a href="http://www.lovemytool.com/blog/2012/01/wireshark-using-configuration-profiles-by-joke-snelders.html">Using Configuration Profiles</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '13, 10:26</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div></div><div id="comments-container-20584" class="comments-container"><span id="20587"></span><div id="comment-20587" class="comment"><div id="post-20587-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I had already read the UG section on profiles to no avail but your article cleared things up for me. From that I learned that the sequence for me is to create a profile then configure WS the way I want it to behave for that profile. I was going about that backwards, configuring WS first then trying to create/save a new profile.</p><p>One question remains for me, once I've created a new profile and configured WS is the new configuration updated each time I alter something (e.g. add a display column), or are the profile changes updated at some later time such as when exiting WS or starting a new capture?</p></div><div id="comment-20587-info" class="comment-info"><span class="comment-age">(18 Apr '13, 12:28)</span> gismo</div></div><span id="20590"></span><div id="comment-20590" class="comment"><div id="post-20590-score" class="comment-score"></div><div class="comment-text"><p>The new configuration is updated right away.<br />
See C:\Documents and Settings\user\Application Data\Wireshark\Profiles\your_profile\preferences<br />
<br />
Note<br />
When you have multiple instances of Wireshark running at the same time, the changes are not updated in the other instances right away.<br />
To update them, you can for instance:<br />
- close and open the file in the other instance<br />
- switch to the default profile and back to your_profile<br />
Thank you:)<br />
</p></div><div id="comment-20590-info" class="comment-info"><span class="comment-age">(18 Apr '13, 13:11)</span> joke</div></div></div><div id="comment-tools-20584" class="comment-tools"></div><div class="clear"></div><div id="comment-20584-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

