+++
type = "question"
title = "Older version"
description = '''I currently have an older version of wireshark installed on my PC, I was wondering should I install a newer version right over the top of the older version or uninstall the older version first and then install the newer version.'''
date = "2013-02-28T18:18:00Z"
lastmod = "2013-03-01T10:26:00Z"
weight = 18995
keywords = [ "version" ]
aliases = [ "/questions/18995" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Older version](/questions/18995/older-version)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18995-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18995-score" class="post-score" title="current number of votes">0</div><span id="post-18995-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I currently have an older version of wireshark installed on my PC, I was wondering should I install a newer version right over the top of the older version or uninstall the older version first and then install the newer version.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '13, 18:18</strong></p><img src="https://secure.gravatar.com/avatar/03448f5a71ad0563e7fcd9b666410b88?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jimjimalabim&#39;s gravatar image" /><p><span>jimjimalabim</span><br />
<span class="score" title="20 reputation points">20</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jimjimalabim has no accepted answers">0%</span></p></div></div><div id="comments-container-18995" class="comments-container"></div><div id="comment-tools-18995" class="comment-tools"></div><div class="clear"></div><div id="comment-18995-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19011"></span>

<div id="answer-container-19011" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19011-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19011-score" class="post-score" title="current number of votes">2</div><span id="post-19011-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jimjimalabim has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can simply install the newer version over the top of what is already installed. Wireshark is smart enough to do the uninstall for you first. By default it saves all your settings, unless you choose to override that. For most people the whole process is simply a matter of repeatedly hitting 'enter' until done, although you'll want to move through it slowly the first time you do it so you can verify what's going on. Easy peasy!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '13, 22:06</strong></p><img src="https://secure.gravatar.com/avatar/b260fb38b621169269b5030f1ed6b766?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="griff&#39;s gravatar image" /><p><span>griff</span><br />
<span class="score" title="361 reputation points">361</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="griff has 2 accepted answers">10%</span></p></div></div><div id="comments-container-19011" class="comments-container"><span id="19048"></span><div id="comment-19048" class="comment"><div id="post-19048-score" class="comment-score"></div><div class="comment-text"><p>Thanks griff. For anyone else reading this and wondering the same thing here is my answer right in the wireshark user's guide. I guess I should have read a little before asking a question</p><pre><code>Building and Installing Wireshark 18
2.8.3. Update Wireshark From time to time you may want to update your installed Wireshark to a more recent version. If you join Wireshark&#39;s announce mailing list, you will be informed about new Wireshark versions, see Section 1.6.5, “Mailing Lists” for details how to subscribe to this list. New versions of Wireshark usually become available every 4 to 8 months. Updating Wireshark is done the same way as installing it, you simply download and start the installer exe. A reboot is usually not required and all your personal settings remain unchanged.
2.8.4. Update WinPcap New versions of WinPcap are less frequently available, maybe only once in a year. You will find WinPcap update instructions where you can download new WinPcap versions. Usually you have to reboot the machine after installing a new WinPcap version. Warning! If you have an older version of WinPcap installed, you must uninstall it before installing the current version. Recent versions of the WinPcap installer will take care of this.
2.8.5. Uninstall Wireshark You can uninstall Wireshark the usual way, using the &quot;Add or Remove Programs&quot; option inside the Control Panel. Select the &quot;Wireshark&quot; entry to start the uninstallation procedure. The Wireshark uninstaller will provide several options as to which things are to be uninstalled; the default is to remove the core components but keep the personal settings, WinPcap and alike. WinPcap won&#39;t be uninstalled by default, as other programs than Wireshark may use it as well.
2.8.6. Uninstall WinPcap You can uninstall WinPcap independently of Wireshark, using the &quot;WinPcap&quot; entry in the &quot;Add or Remove Programs&quot; of the Control Panel. Note! After uninstallation of WinPcap you can&#39;t capture anything with Wireshark. It might be a good idea to reboot Windows afterwards</code></pre></div><div id="comment-19048-info" class="comment-info"><span class="comment-age">(01 Mar '13, 10:26)</span> <span class="comment-user userinfo">jimjimalabim</span></div></div></div><div id="comment-tools-19011" class="comment-tools"></div><div class="clear"></div><div id="comment-19011-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

