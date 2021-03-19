+++
type = "question"
title = "Prevent Patch file from getting outdated"
description = '''Hi guys, I have finished developing(on Ubuntu 12.4) my second dissector for Wireshark as a plugin and made a patch file(.diff). However, when I went to patch the Wireshark source, obtained by &#x27;svn co http://anonsvn.wireshark.org/wireshark/trunk/&#x27;, the patch failed because the source had been updated...'''
date = "2012-07-10T07:45:00Z"
lastmod = "2012-07-12T19:46:00Z"
weight = 12559
keywords = [ "dissector", "plugin", "patch" ]
aliases = [ "/questions/12559" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Prevent Patch file from getting outdated](/questions/12559/prevent-patch-file-from-getting-outdated)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12559-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12559-score" class="post-score" title="current number of votes">0</div><span id="post-12559-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>I have finished developing(on Ubuntu 12.4) my second dissector for Wireshark as a plugin and made a patch file(.diff). However, when I went to patch the Wireshark source, obtained by 'svn co <a href="http://anonsvn.wireshark.org/wireshark/trunk/&#39;,">http://anonsvn.wireshark.org/wireshark/trunk/',</a> the patch failed because the source had been updated to not include one of the plugins it used to and that I have on my main computer("giop" is the name). I know a way to fix this issue, I will just go in manually and add my dissectors as plugins but this defeats the whole purpose of the patch file. The version of the source on my main computer is only a month or two old. Is there any better way to make a patch file or something like it? I would hate to have to go through manually every month or so and re add all my dissectors.</p><p>My thought right now is to just download the source and save it to my drive and use the same source every time when I want to put it on a new computer. Any other ideas or critiques of mine would be greatly appreciated!</p><p>Thanks, Thomas</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span> <span class="post-tag tag-link-patch" rel="tag" title="see questions tagged &#39;patch&#39;">patch</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '12, 07:45</strong></p><img src="https://secure.gravatar.com/avatar/03b95706bb0738803b4c9c0c9d75cf52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hildesht&#39;s gravatar image" /><p><span>hildesht</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hildesht has no accepted answers">0%</span></p></div></div><div id="comments-container-12559" class="comments-container"><span id="12560"></span><div id="comment-12560" class="comment"><div id="post-12560-score" class="comment-score"></div><div class="comment-text"><p>Just realized that I should probably be using a release version of Wireshark and not the trunk version. I'm assuming the trunk version is more of a developmental version, correct me if I am wrong but I hope switching to this will help.</p></div><div id="comment-12560-info" class="comment-info"><span class="comment-age">(10 Jul '12, 07:50)</span> <span class="comment-user userinfo">hildesht</span></div></div></div><div id="comment-tools-12559" class="comment-tools"></div><div class="clear"></div><div id="comment-12559-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12570"></span>

<div id="answer-container-12570" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12570-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12570-score" class="post-score" title="current number of votes">2</div><span id="post-12570-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hildesht has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Correct: the stable/release versions are, well, more stable (meaning: less things change) so sticking to a release branch (the current one is trunk-1.8) is a good idea.</p><p>An even better idea would be to clean up your dissector and submit it to Wireshark so maintaining it becomes the core developers' job. :-)</p><p>(That being said, yes, I, too, maintain a number of "private" dissectors; I usually figure the punishment for this "sin" is having to maintain them myself.)</p><p>Also: the GIOP dissector did not go away, it was simply moved from being a plugin to being a built-in dissector (in epan/dissectors/ instead of plugins/giop).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '12, 12:21</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-12570" class="comments-container"><span id="12663"></span><div id="comment-12663" class="comment"><div id="post-12663-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the information! So far I have made 2 dissectors as plugins. One for the commands sent to the <a href="http://ardrone.parrot.com/parrot-ar-drone/usa/">Parrot AR Drone</a> (a quad copter that is available commercially) and a dissector for the <a href="http://qgroundcontrol.org/mavlink/start">MAVLink protocol</a> that is used by arduPlanes. Do you think anyone else would be interested in these? I would like to share my work with the community but only if this is something that would be helpful.</p><p>Thanks, Thomas</p></div><div id="comment-12663-info" class="comment-info"><span class="comment-age">(12 Jul '12, 10:53)</span> <span class="comment-user userinfo">hildesht</span></div></div><span id="12675"></span><div id="comment-12675" class="comment"><div id="post-12675-score" class="comment-score"></div><div class="comment-text"><p>Well, one never knows. There are a LOT of protocol dissectors in Wireshark that are really quite specialized. Chances are if you're interested in dissecting those packets, somebody else will be too at some point or another. See this page for instructions on submitting your dissector(s) if you choose to do so:</p><p><a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSrcContribute.html">http://www.wireshark.org/docs/wsdg_html_chunked/ChSrcContribute.html</a></p></div><div id="comment-12675-info" class="comment-info"><span class="comment-age">(12 Jul '12, 15:57)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="12676"></span><div id="comment-12676" class="comment"><div id="post-12676-score" class="comment-score"></div><div class="comment-text"><p>Remote-controlled planes sound like major nerd magnets, so I can imagine <em>significant</em> interest in dissecting both protocols by Wireshark users (I'm guessing the "ardu" in "arduPlanes" refers to Arduino, so we're <em>definitely</em> talking nerd magnet :-)). As such, both dissectors would probably be worthwhile additions to Wireshark for at least some users.</p></div><div id="comment-12676-info" class="comment-info"><span class="comment-age">(12 Jul '12, 19:46)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-12570" class="comment-tools"></div><div class="clear"></div><div id="comment-12570-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

