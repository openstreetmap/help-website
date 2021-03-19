+++
type = "question"
title = "Couldn&#x27;t load module....specified module cannot be found."
description = '''I downloaded and installed Wireshark 1.8.0 executable (win32). Its runs without a problem. I have a custom dissector that I have been using since at least Wireshark 1.4.x. I downloaded the 1.8.0 source and compiled it and my dissector. I ran Wireshark out of the gtk2 subdirectory; and it ran great, ...'''
date = "2012-06-25T11:29:00Z"
lastmod = "2012-06-28T01:51:00Z"
weight = 12153
keywords = [ "development", "windows", "error" ]
aliases = [ "/questions/12153" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Couldn't load module....specified module cannot be found.](/questions/12153/couldnt-load-modulespecified-module-cannot-be-found)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12153-score" class="post-score" title="current number of votes">0</div><span id="post-12153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I downloaded and installed Wireshark 1.8.0 executable (win32). Its runs without a problem.</p><p>I have a custom dissector that I have been using since at least Wireshark 1.4.x. I downloaded the 1.8.0 source and compiled it and my dissector. I ran Wireshark out of the <code>gtk2</code> subdirectory; and it ran great, and my dissector had no issues.</p><p>I copied my dissector (adsb.dll) to <code>C:\Program Files\Wireshark\plugins\1.8.0\</code>, where my downloaded Wireshark resides. Then, I ran Wireshark and got an error box, telling me:</p><blockquote><p><code>Couldn't load module C:\Program Files\Wireshark\plugins\1.8.0\adsb.dll: 'C:\Program Files\Wireshark\plugins\1.8.0\adsb.dll': The specified module could not be found</code></p></blockquote><p>Puzzled, I took my adsb.dll that was compiled against Wireshark 1.6.5 and put that in the 1.8.0 directory. That too has the same error message. Being that I've used this dissector with no errors as recently as 2 days ago and that the source hasn't been modified since January, I have to believe Wireshark 1.8.0 is behaving differently.</p><p>Once again, the dissector and Wireshark run fine out of the <code>gtk2</code> subdirectory, but once I move the plugin into stock Wireshark 1.8.0, it cannot load the module without giving me a vague error.</p><p>Any help is certainly appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jun '12, 11:29</strong></p><img src="https://secure.gravatar.com/avatar/b363fb1dfec547bd68fa5e3eae8836a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike_P&#39;s gravatar image" /><p><span>Mike_P</span><br />
<span class="score" title="30 reputation points">30</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike_P has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Jun '12, 19:43</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-12153" class="comments-container"></div><div id="comment-tools-12153" class="comment-tools"></div><div class="clear"></div><div id="comment-12153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12165"></span>

<div id="answer-container-12165" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12165-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12165-score" class="post-score" title="current number of votes">2</div><span id="post-12165-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The message can be generated due to several reasons. Can you please check:</p><p>manifest<br />
<a href="http://www.wireshark.org/lists/wireshark-dev/200902/msg00012.html">http://www.wireshark.org/lists/wireshark-dev/200902/msg00012.html</a><br />
</p><p>compiler version. What did you use?<br />
<a href="http://www.mail-archive.com/wireshark-dev@wireshark.org/msg08764.html">http://www.mail-archive.com/<span class="__cf_email__" data-cfemail="e3948a9186908b829188ce878695a3948a9186908b829188cd8c9184">[email protected]</span>/msg08764.html</a></p><p>vc++ redistributable<br />
<a href="http://ask.wireshark.org/questions/5377/dissector-runs-on-my-computer-but-not-others">http://ask.wireshark.org/questions/5377/dissector-runs-on-my-computer-but-not-others</a><br />
</p><p>If that does not help, please file a bug report on <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and attach the plugin DLL.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '12, 02:14</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Jun '12, 02:17</strong> </span></p></div></div><div id="comments-container-12165" class="comments-container"><span id="12207"></span><div id="comment-12207" class="comment"><div id="post-12207-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the feedback.</p><p>I decided to kind of go that route. I was running Visual C++ 2008 Express. I bumped up to 2010 Express to try to see if that helped. It took a bit of wrangling to get it working since Windows did not like having different versions of things with service packs applied on my XP box. But that indeed solved the problem once I went to 2010 Express.</p><p>My Win 7 x64 box was a different matter. I had to completely uninstall 2008 Express and any traces of the redistributable and only then could I remove the Win7 SDK 7 so I could upgrade to 7.1 and SP1. After I got that done, I could upgrade to C++ 2010 Express.</p><p>Which I forgot does not natively support x64 compiling. Regardless, I got that working, too. In the end, upgrading to Visual C++ 2010 Express on my x86 and x64 boxes solved my problem of compiling my dissector and using it with the stock 1.8.0 version of Wireshark.</p></div><div id="comment-12207-info" class="comment-info"><span class="comment-age">(26 Jun '12, 13:28)</span> <span class="comment-user userinfo">Mike_P</span></div></div><span id="12262"></span><div id="comment-12262" class="comment"><div id="post-12262-score" class="comment-score"></div><div class="comment-text"><p>Wireshark 1.8.0:</p><blockquote><p><code>Built using Microsoft Visual C++ 10.0 build 40219</code><br />
</p></blockquote><p>Wireshark 1.6.8:</p><blockquote><p><code>Built using Microsoft Visual C++ 9.0 build 21022</code></p></blockquote><p>That should explain your problems.</p></div><div id="comment-12262-info" class="comment-info"><span class="comment-age">(28 Jun '12, 01:51)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-12165" class="comment-tools"></div><div class="clear"></div><div id="comment-12165-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

