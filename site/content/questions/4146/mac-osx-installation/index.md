+++
type = "question"
title = "Mac OSX Installation"
description = '''I&#x27;ve having an issue installing Wireshark on my MacBook Pro. I&#x27;ve read the Readme documentation and believe I have done the necessary steps, but it won&#x27;t startup. Steps 3 and 4 are a little fuzzy. Can someone please explain in further detail?  Drag the contents of the Command Line folder to $HOME/bi...'''
date = "2011-05-19T11:10:00Z"
lastmod = "2011-05-19T16:51:00Z"
weight = 4146
keywords = [ "osx", "mac", "installation" ]
aliases = [ "/questions/4146" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mac OSX Installation](/questions/4146/mac-osx-installation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4146-score" class="post-score" title="current number of votes">0</div><span id="post-4146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've having an issue installing Wireshark on my MacBook Pro. I've read the Readme documentation and believe I have done the necessary steps, but it won't startup. Steps 3 and 4 are a little fuzzy. Can someone please explain in further detail?</p><ol><li>Drag the contents of the Command Line folder to $HOME/bin, /usr/local/bin, /opt/wireshark/bin or any other location that makes sense (preferably one that's in your PATH).<ol><li>You will probably need to adjust the permissions of /dev/bpf* in order to capture. You can do this by hand or by dragging the ChmodBPF folder onto the StartupItems alias.</li></ol></li></ol></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '11, 11:10</strong></p><img src="https://secure.gravatar.com/avatar/93e79232f218df3df8f39cc6194996de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jblancids&#39;s gravatar image" /><p><span>jblancids</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jblancids has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> retagged <strong>27 May '11, 20:56</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-4146" class="comments-container"><span id="4157"></span><div id="comment-4157" class="comment"><div id="post-4157-score" class="comment-score"></div><div class="comment-text"><p>Do you mean Wireshark won't start at all, or that it won't do a capture? If it won't start at all, the ChmodBPF stuff won't make a difference.</p><p>Do any messages get logged in Console (use "All Messages") when you try to start Wireshark?</p></div><div id="comment-4157-info" class="comment-info"><span class="comment-age">(19 May '11, 16:51)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-4146" class="comment-tools"></div><div class="clear"></div><div id="comment-4146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4156"></span>

<div id="answer-container-4156" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4156-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4156-score" class="post-score" title="current number of votes">0</div><span id="post-4156-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Does this help? <a href="http://article.gmane.org/gmane.network.wireshark.devel/20997">http://article.gmane.org/gmane.network.wireshark.devel/20997</a></p><p>There have been quite a few other Mac OSX related installation &amp; capturing problems reported on this site as well. Here are a few more you might want to look through in case the above link doesn't help or if you are just curious:</p><ul><li><a href="http://ask.wireshark.org/questions/578/mac-os-cant-detect-any-interface">http://ask.wireshark.org/questions/578/mac-os-cant-detect-any-interface</a></li><li><a href="http://ask.wireshark.org/questions/858/encountering-an-error-when-starting-a-new-capture-on-mac-osx">http://ask.wireshark.org/questions/858/encountering-an-error-when-starting-a-new-capture-on-mac-osx</a></li><li><a href="http://ask.wireshark.org/questions/1218/cant-find-an-interface-in-order-to-capture">http://ask.wireshark.org/questions/1218/cant-find-an-interface-in-order-to-capture</a></li><li><a href="http://ask.wireshark.org/questions/2405/mac-osx-installation">http://ask.wireshark.org/questions/2405/mac-osx-installation</a></li><li><a href="http://ask.wireshark.org/questions/2829/capturing-with-wireshark-on-mac-os-1066">http://ask.wireshark.org/questions/2829/capturing-with-wireshark-on-mac-os-1066</a></li><li><a href="http://ask.wireshark.org/questions/2912/mac-osx-install-problems">http://ask.wireshark.org/questions/2912/mac-osx-install-problems</a></li><li><a href="http://ask.wireshark.org/questions/3536/no-interface-available-to-capture">http://ask.wireshark.org/questions/3536/no-interface-available-to-capture</a></li></ul><p>Finally, <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5756">bug 5756</a> may be of interest to you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '11, 16:22</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 May '11, 16:24</strong> </span></p></div></div><div id="comments-container-4156" class="comments-container"></div><div id="comment-tools-4156" class="comment-tools"></div><div class="clear"></div><div id="comment-4156-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

