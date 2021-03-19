+++
type = "question"
title = "[SOLVED] How to generate Wireshark Binary package for Linux"
description = '''Hi all, I read the developer guide , chapter 3.12 &quot;Binary Packaging&quot; but there are only MAC OS, WIN32. I don&#x27;t know whether Debian and Red hat are used for Linux or not. So, could you please tell me how to generate &quot;set up&quot; file for Linux and where it is generated. Thank you so much'''
date = "2013-09-16T01:23:00Z"
lastmod = "2013-09-18T08:26:00Z"
weight = 24736
keywords = [ "binary", "build", "linux" ]
aliases = [ "/questions/24736" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\[SOLVED\] How to generate Wireshark Binary package for Linux](/questions/24736/solved-how-to-generate-wireshark-binary-package-for-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24736-score" class="post-score" title="current number of votes">0</div><span id="post-24736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I read the developer guide , chapter 3.12 "Binary Packaging" but there are only MAC OS, WIN32. I don't know whether Debian and Red hat are used for Linux or not. So, could you please tell me how to generate "set up" file for Linux and where it is generated. Thank you so much</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-binary" rel="tag" title="see questions tagged &#39;binary&#39;">binary</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '13, 01:23</strong></p><img src="https://secure.gravatar.com/avatar/824a7342f59ff90e6040505b38626416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoangsonk49&#39;s gravatar image" /><p><span>hoangsonk49</span><br />
<span class="score" title="81 reputation points">81</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoangsonk49 has 2 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Sep '13, 02:57</strong> </span></p></div></div><div id="comments-container-24736" class="comments-container"></div><div id="comment-tools-24736" class="comment-tools"></div><div class="clear"></div><div id="comment-24736-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24741"></span>

<div id="answer-container-24741" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24741-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24741-score" class="post-score" title="current number of votes">2</div><span id="post-24741-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hoangsonk49 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From <a href="http://anonsvn.wireshark.org/wireshark/trunk/INSTALL">INSTALL</a> in the root of the source directory:</p><pre><code>9. Run &#39;make install&#39;.  If you&#39;re running a system that supports
   the Apt, RPM, OSX, or System V Release 4 packaging systems, you can
   run one of

        make debian-package # Builds a binary package using dpkg
        make rpm-package    # Builds a binary package using rpm
        make srpm-package   # Builds a source package using rpm
        make svr4-package   # Builds a binary package using pkgmk
        make solaris-package    # Same as &quot;make svr4-package&quot;
        make osx-package    # Builds a binary package for OSX

   to make an installable package for your system.</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '13, 02:31</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-24741" class="comments-container"><span id="24742"></span><div id="comment-24742" class="comment"><div id="post-24742-score" class="comment-score"></div><div class="comment-text"><p>Do you know where it is generated? For Window package, I see that the developer guide mention the location but for Linux, I don't see anything. Thanks, grahamb!</p></div><div id="comment-24742-info" class="comment-info"><span class="comment-age">(16 Sep '13, 03:00)</span> <span class="comment-user userinfo">hoangsonk49</span></div></div><span id="24755"></span><div id="comment-24755" class="comment"><div id="post-24755-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>find . -name *.rpm</p></blockquote></div><div id="comment-24755-info" class="comment-info"><span class="comment-age">(16 Sep '13, 06:38)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="24786"></span><div id="comment-24786" class="comment"><div id="post-24786-score" class="comment-score"></div><div class="comment-text"><p>OK, thanks Kurt. I will try it in this afternoon</p></div><div id="comment-24786-info" class="comment-info"><span class="comment-age">(16 Sep '13, 18:38)</span> <span class="comment-user userinfo">hoangsonk49</span></div></div><span id="24919"></span><div id="comment-24919" class="comment"><div id="post-24919-score" class="comment-score"></div><div class="comment-text"><p>BTW there's no need to update the Question title when you accept an answer. Just click the checkbox to Accept an answer.</p><p>(If you update the title of the question the question appears to get pushed to RSS feeds again :-( )</p></div><div id="comment-24919-info" class="comment-info"><span class="comment-age">(18 Sep '13, 08:26)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-24741" class="comment-tools"></div><div class="clear"></div><div id="comment-24741-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

