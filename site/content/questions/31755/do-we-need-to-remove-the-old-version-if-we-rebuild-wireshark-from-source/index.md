+++
type = "question"
title = "Do we need to remove the old version if we rebuild wireshark from source?"
description = '''Hey, This must be a &quot;duh!&quot; question to some, but not me.  I built Wireshark from source (from nightly builds) in Ubuntu 12.04. Now I want to get the latest source and rebuild. Do I need to remove the old version? And if I do, what&#x27;s the best way to do it? (I saw that if I simply installing from Wire...'''
date = "2014-04-11T09:01:00Z"
lastmod = "2014-04-14T12:34:00Z"
weight = 31755
keywords = [ "source", "old", "from", "build", "remove" ]
aliases = [ "/questions/31755" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Do we need to remove the old version if we rebuild wireshark from source?](/questions/31755/do-we-need-to-remove-the-old-version-if-we-rebuild-wireshark-from-source)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31755-score" class="post-score" title="current number of votes">0</div><span id="post-31755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey,</p><p>This must be a "duh!" question to some, but not me.<br />
</p><p>I built Wireshark from source (from nightly builds) in Ubuntu 12.04. Now I want to get the latest source and rebuild. Do I need to remove the old version? And if I do, what's the best way to do it? (I saw that if I simply installing from Wireshark binaries from nightly build to nightly build, I don't need to remove the older version)</p><p>Here is the steps I took in building from source the first time, which may help answer my question a bit, and please give suggestions if you see any steps not done in the optimal way.</p><ol><li>Download source</li><li>Unpack and move the unpacked directory into home directory.</li><li>Change into that directory</li><li>Repeatedly do ./configure to figure out what dependent software is not installed and install them.</li><li>finally do ./configure —with-lua (since I need Lua)</li><li>make</li><li>make install</li></ol><p>I totally didn't do the autogen.sh step, which I will do this time before ./configure. (Wireshark still worked without this step though).</p><p>When I tried to launch Wireshark for the first time after compiling, I got an error saying libfiretap.so.0 cannot open. Apparently "sudo ldconfig" command fixed it, but I'm not sure if this is a hack fix. This error probably won't happen if I compiled the source better, or put them in different directories.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-source" rel="tag" title="see questions tagged &#39;source&#39;">source</span> <span class="post-tag tag-link-old" rel="tag" title="see questions tagged &#39;old&#39;">old</span> <span class="post-tag tag-link-from" rel="tag" title="see questions tagged &#39;from&#39;">from</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-remove" rel="tag" title="see questions tagged &#39;remove&#39;">remove</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '14, 09:01</strong></p><img src="https://secure.gravatar.com/avatar/b18cada3e3589f311e24f5ffbd1737bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YXI&#39;s gravatar image" /><p><span>YXI</span><br />
<span class="score" title="21 reputation points">21</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YXI has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-31755" class="comments-container"></div><div id="comment-tools-31755" class="comment-tools"></div><div class="clear"></div><div id="comment-31755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31757"></span>

<div id="answer-container-31757" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31757-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31757-score" class="post-score" title="current number of votes">0</div><span id="post-31757-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming you are downloading an archive of the sources and then expanding it over the top of an existing source tree, then it is best to do the complete re-compile dance.</p><p>You may want to look into getting the source via git. This also allows you to track any changes you might make, and pull in any other changes posted elsewhere, e.g. <a href="https://code.wireshark.org/review/#/q/status:open,n,z">Wireshark Gerrit</a>. Look at the <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSrcObtain.html">Developers Guide</a> for more info on obtaining the source code.</p><p>You might also consider building using CMake, as that does "out-of-tree" builds, i.e. the object files and libraries are compiled in a separate directory from the sources. See <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=README.cmake">README.cmake</a> in the source docs directoyr.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '14, 09:20</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Apr '14, 09:21</strong> </span></p></div></div><div id="comments-container-31757" class="comments-container"><span id="31762"></span><div id="comment-31762" class="comment"><div id="post-31762-score" class="comment-score"></div><div class="comment-text"><p>OK, you are dragging me toward the developer's side. I want to just stay on the user side, at least for now. : o ) If I do rebuild all the time, obviously it's much easier to use git and get the newest code and compile. But I don't think I will be rebuilding that often (hopefully), and so far I'm happy downloading source from: <a href="http://www.wireshark.org/download/automated/src/,">http://www.wireshark.org/download/automated/src/,</a> which has everything.<br />
I guess my question is (for a lazy bum), can I just redownlaod from this link and recompile? Is it best to remove the earlier version first? If so, before removing the whole folder, do I need to do anything else, like make uninstall? I guess this is more a Linux question than a Wireshark question, but I think I will get a better answer here.</p></div><div id="comment-31762-info" class="comment-info"><span class="comment-age">(11 Apr '14, 14:47)</span> <span class="comment-user userinfo">YXI</span></div></div><span id="31766"></span><div id="comment-31766" class="comment"><div id="post-31766-score" class="comment-score"></div><div class="comment-text"><p>If you've installed then it's best to uninstall, hopefully that will remove all traces of the previous installation so that your brand new compilation won't pick up old shared libraries, e.g. plugins.</p><p>You might not run into any such issues, but probably best to be hygienic with the file system.</p></div><div id="comment-31766-info" class="comment-info"><span class="comment-age">(12 Apr '14, 03:04)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="31799"></span><div id="comment-31799" class="comment"><div id="post-31799-score" class="comment-score"></div><div class="comment-text"><p>Just did a "sudo make uninstall" in the source directory and all Wireshark related libraries are gone.<br />
This should probably be added to the official INSTALL file in the distribution source tarball.<br />
Thanks.</p></div><div id="comment-31799-info" class="comment-info"><span class="comment-age">(14 Apr '14, 12:34)</span> <span class="comment-user userinfo">YXI</span></div></div></div><div id="comment-tools-31757" class="comment-tools"></div><div class="clear"></div><div id="comment-31757-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

