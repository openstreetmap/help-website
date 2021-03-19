+++
type = "question"
title = "OS X Lion Install failure"
description = '''Hi,  I&#x27;m having trouble running Wireshark on Mac OS X 10.7.1 Lion - The Install seems to proceed ok, but on running Wireshark I get a window warning me the app may take time to start the first time as the font caches are built, but then it quits.  I had a previous version installed, but I have clean...'''
date = "2011-10-07T05:52:00Z"
lastmod = "2012-06-21T21:19:00Z"
weight = 6780
keywords = [ "osx", "lion", "startup", "mac" ]
aliases = [ "/questions/6780" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OS X Lion Install failure](/questions/6780/os-x-lion-install-failure)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6780-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6780-score" class="post-score" title="current number of votes">0</div><span id="post-6780-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm having trouble running Wireshark on Mac OS X 10.7.1 Lion - The Install seems to proceed ok, but on running Wireshark I get a window warning me the app may take time to start the first time as the font caches are built, but then it quits.</p><p>I had a previous version installed, but I have cleaned out /Applications/Wireshark, /Library/StartupItems/ChmodBPF and /opt/local/bin/wireshark (remnant from a previous Macports install) - but there was no /Library/Wireshark.</p><p>Attempting a reinstallation has no effect, and while /Applications/Wireshark and /Library/StartupItems/ChmodBPF are created again, /Library/Wireshark is not. Behaviour on staring Wireshark is the same - notification message about font caches, and then quit. This happens on subsequent launches of Wireshark too.</p><p>Any ideas or advice?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-lion" rel="tag" title="see questions tagged &#39;lion&#39;">lion</span> <span class="post-tag tag-link-startup" rel="tag" title="see questions tagged &#39;startup&#39;">startup</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Oct '11, 05:52</strong></p><img src="https://secure.gravatar.com/avatar/e5c24d2187f4342f27122afb329efb33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="James%20Dore&#39;s gravatar image" /><p><span>James Dore</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="James Dore has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Oct '11, 06:53</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6780" class="comments-container"></div><div id="comment-tools-6780" class="comment-tools"></div><div class="clear"></div><div id="comment-6780-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6784"></span>

<div id="answer-container-6784" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6784-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6784-score" class="post-score" title="current number of votes">1</div><span id="post-6784-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Aha: <code>Console.app</code> proved instructive:</p><pre><code>07/10/2011 12:20:15.112 [0x0-0x314314].org.wireshark.Wireshark: touch: /Users/james/.wireshark/.fccache-new: Permission denied</code></pre><p>The directory (<code>/User/james/.wireshark</code>) was owned by <code>root</code> (probably from the MacPorts install), so I changed its ownership to <code>james</code> with this command:</p><pre><code>sudo chown -R james /Users/james/.wireshark</code></pre><p>It now starts and runs as normal.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '11, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/e5c24d2187f4342f27122afb329efb33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="James%20Dore&#39;s gravatar image" /><p><span>James Dore</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="James Dore has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jun '12, 21:40</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6784" class="comments-container"><span id="12120"></span><div id="comment-12120" class="comment"><div id="post-12120-score" class="comment-score"></div><div class="comment-text"><p>I dont understand this answer can someone else provide more info. what did the job?</p></div><div id="comment-12120-info" class="comment-info"><span class="comment-age">(21 Jun '12, 19:21)</span> <span class="comment-user userinfo">sharkyf</span></div></div><span id="12123"></span><div id="comment-12123" class="comment"><div id="post-12123-score" class="comment-score">1</div><div class="comment-text"><p>I think this is a good explanation (someone feel free to correct me):</p><p>The user installed <code>wireshark</code> via <a href="www.macports.org">MacPorts</a>, which installs all files and directories* as <code>root</code>, and thus the files and directories are owned by <code>root</code>. One of the directories MacPorts creates during the installation is <code>~/.wireshark</code>. When the user <code>james</code> tries to start Wireshark, it loads <code>libfontconfig</code>, which tries to create a new font cache at <code>~/.wireshark/.fccache-new</code>, but the directory's permissions presumably allowed write-access only to the owner (<code>root</code>), preventing the user <code>james</code> from creating files there (thus the error: <code>Permission denied</code>).</p><p>To compensate, <span></span><span>@James Dore</span> changed the ownership of the directory <code>~/.wireshark/</code> to the user <code>james</code> so that Wireshark (running as <code>james</code>) could create the font cache as needed.</p><p><sub><em>*Is it really all files? I think so.</em></sub></p></div><div id="comment-12123-info" class="comment-info"><span class="comment-age">(21 Jun '12, 21:19)</span> <span class="comment-user userinfo">helloworld</span></div></div></div><div id="comment-tools-6784" class="comment-tools"></div><div class="clear"></div><div id="comment-6784-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

