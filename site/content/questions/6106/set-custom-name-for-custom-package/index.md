+++
type = "question"
title = "Set Custom name for Custom Package"
description = '''I have gone through the steps of Win32 step by step guide.I have also made a package of Wireshark but the setup package has Wireshark as its name and tooltip.Also the dialog boxes open while installing this custom made package are having title as wireshark in them. How to set a user defined name for...'''
date = "2011-09-05T23:49:00Z"
lastmod = "2011-09-06T03:39:00Z"
weight = 6106
keywords = [ "packaging" ]
aliases = [ "/questions/6106" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Set Custom name for Custom Package](/questions/6106/set-custom-name-for-custom-package)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6106-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6106-score" class="post-score" title="current number of votes">0</div><span id="post-6106-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have gone through the steps of Win32 step by step guide.I have also made a package of Wireshark but the setup package has Wireshark as its name and tooltip.Also the dialog boxes open while installing this custom made package are having title as wireshark in them. How to set a user defined name for custom packed wireshark by default?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packaging" rel="tag" title="see questions tagged &#39;packaging&#39;">packaging</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Sep '11, 23:49</strong></p><img src="https://secure.gravatar.com/avatar/968cc7ddfc48322ffbd1d7f5e3d37b85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terrestrial%20shark&#39;s gravatar image" /><p><span>Terrestrial ...</span><br />
<span class="score" title="96 reputation points">96</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terrestrial shark has 3 accepted answers">42%</span></p></div></div><div id="comments-container-6106" class="comments-container"><span id="6112"></span><div id="comment-6112" class="comment"><div id="post-6112-score" class="comment-score"></div><div class="comment-text"><p>Are you just wanting to show it's a custom version of Wireshark or remove references to Wireshark entirely?</p></div><div id="comment-6112-info" class="comment-info"><span class="comment-age">(06 Sep '11, 00:54)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="6116"></span><div id="comment-6116" class="comment"><div id="post-6116-score" class="comment-score"></div><div class="comment-text"><p>i like to replace the word wireshark on the wireshark installer, installer's tooltip,installer dialog boxes that are opened while installing,with any other xyz and try.</p><p>check 2.2.13 option in the below given html page.</p><p>http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html</p></div><div id="comment-6116-info" class="comment-info"><span class="comment-age">(06 Sep '11, 01:27)</span> <span class="comment-user userinfo">Terrestrial ...</span></div></div></div><div id="comment-tools-6106" class="comment-tools"></div><div class="clear"></div><div id="comment-6106-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6117"></span>

<div id="answer-container-6117" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6117-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6117-score" class="post-score" title="current number of votes">2</div><span id="post-6117-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Terrestrial shark has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To change the installer info you'll need to edit <code>packaging\nsis\wireshark.nsi</code> and possibly some of the files referenced by that file. The item you point to in the Developers Guide just refers to the name of the installer executable produced by modifying <code>VERSION_EXTRA</code> in config.nmake.</p><p>Out of interest why do you want to lose the cachet associated with the Wireshark brand by replacing it with something else?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '11, 02:01</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-6117" class="comments-container"><span id="6120"></span><div id="comment-6120" class="comment"><div id="post-6120-score" class="comment-score"></div><div class="comment-text"><p>please answer my other two questions too..</p><p>Thanks, Regards, Prashanth.</p></div><div id="comment-6120-info" class="comment-info"><span class="comment-age">(06 Sep '11, 03:39)</span> <span class="comment-user userinfo">Terrestrial ...</span></div></div></div><div id="comment-tools-6117" class="comment-tools"></div><div class="clear"></div><div id="comment-6117-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

