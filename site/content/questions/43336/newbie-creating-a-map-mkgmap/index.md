+++
type = "question"
title = "Newbie Creating a Map (mkgmap)"
description = '''Hi,  I&#x27;m following this page https://wiki.openstreetmap.org/wiki/Mkgmap/help/How_to_create_a_map tutorial. Unfortunately I don&#x27;t get very far. I&#x27;ve installed java 1.7 on Ubuntu 12.04. I&#x27;ve downloaded splitter-r423.jar and us-northeast-latest.osm.pbf to ~/Project$. I then run $ java -jar splitter-r42...'''
date = "2015-05-31T03:42:00Z"
lastmod = "2015-05-31T09:10:00Z"
weight = 43336
keywords = [ "mkgmap", "classpath", "ubuntu" ]
aliases = [ "/questions/43336" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Newbie Creating a Map (mkgmap)](/questions/43336/newbie-creating-a-map-mkgmap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43336-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm following this page <a href="https://wiki.openstreetmap.org/wiki/Mkgmap/help/How_to_create_a_map">https://wiki.openstreetmap.org/wiki/Mkgmap/help/How_to_create_a_map</a> tutorial. Unfortunately I don't get very far. I've installed java 1.7 on Ubuntu 12.04. I've downloaded splitter-r423.jar and us-northeast-latest.osm.pbf to ~/Project$.</p>
<p>I then run $ java -jar splitter-r423.jar us-northeast-latest.osm.pbf</p>
<p>and I get this error: Exception in thread "main" java.lang.NoClassDefFoundError: crosby/binary/file/BlockReaderAdapter at java.lang.Class.getDeclaredMethods0(Native Method) at java.lang.Class.privateGetDeclaredMethods(Class.java:2615) at java.lang.Class.getMethod0(Class.java:2856) at java.lang.Class.getMethod(Class.java:1668) at sun.launcher.LauncherHelper.getMainMethod(LauncherHelper.java:494) at sun.launcher.LauncherHelper.checkAndLoadMain(LauncherHelper.java:486) Caused by: java.lang.ClassNotFoundException: crosby.binary.file.BlockReaderAdapter at java.net.URLClassLoader$1.run(URLClassLoader.java:366) at java.net.URLClassLoader$1.run(URLClassLoader.java:355) at java.security.AccessController.doPrivileged(Native Method) at java.net.URLClassLoader.findClass(URLClassLoader.java:354) at java.lang.ClassLoader.loadClass(ClassLoader.java:425) at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:308) at java.lang.ClassLoader.loadClass(ClassLoader.java:358) ... 6 more I suspect it has to do with classpath but I can't fix it. Could you help? Thank You</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mkgmap" rel="tag" title="see questions tagged &#39;mkgmap&#39;">mkgmap</span> <span class="post-tag tag-link-classpath" rel="tag" title="see questions tagged &#39;classpath&#39;">classpath</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 May '15, 03:42</strong></p>
<img src="https://secure.gravatar.com/avatar/23b2fc8247936643c3615dc9d5980276?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pierre222&#39;s gravatar image" />
<p><span>Pierre222</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pierre222 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 May '15, 21:01</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span></p>
</div>
</div>
<div id="comments-container-43336" class="comments-container">
&#10;</div>
<div id="comment-tools-43336" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43336-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43337"></span>

<div id="answer-container-43337" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43337-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43337-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43337-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think you need to have all splitter files from the zip file, not only the jar file.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 May '15, 09:10</strong></p>
<img src="https://secure.gravatar.com/avatar/0f5ffc3756c4662b9dfad80b7665ac6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ligfietser&#39;s gravatar image" />
<p><span>ligfietser</span><br />
<span class="score" title="2894 reputation points"><span>2.9k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="27 badges"><span class="silver">●</span><span class="badgecount">27</span></span><span title="57 badges"><span class="bronze">●</span><span class="badgecount">57</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ligfietser has 8 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-43337" class="comments-container">
&#10;</div>
<div id="comment-tools-43337" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43337-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

