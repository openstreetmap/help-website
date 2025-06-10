+++
type = "question"
title = "tiles aren&#x27;t being generated"
description = '''I&#x27;m a newbie to much of this, but have been trying to follow directions exactly, with no results. I&#x27;m trying to download a set of tiles for Mapping Tool on my smart phone, using JTileDownloader. Following all the directions I could find, I run JTile... and copy/past the url of the map from OpenStree...'''
date = "2012-03-26T20:01:00Z"
lastmod = "2012-05-08T00:57:00Z"
weight = 11508
keywords = [ "jtiledownloader", "tiles", "java", "generate" ]
aliases = [ "/questions/11508" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [tiles aren't being generated](/questions/11508/tiles-arent-being-generated)

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
<span id="post-11508-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11508-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11508-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm a newbie to much of this, but have been trying to follow directions exactly, with no results. I'm trying to download a set of tiles for Mapping Tool on my smart phone, using JTileDownloader. Following all the directions I could find, I run JTile... and copy/past the url of the map from OpenStreetMap in Permalink format. I set the folder for the output, then click "download tiles", but my destination folder remains empty. I don't see any error messages. Any thoughts on what I'm doing wrong? I'm running version 6 of Java, and 0.6 of JTile... Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-jtiledownloader" rel="tag" title="see questions tagged &#39;jtiledownloader&#39;">jtiledownloader</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-generate" rel="tag" title="see questions tagged &#39;generate&#39;">generate</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Mar '12, 20:01</strong></p>
<img src="https://secure.gravatar.com/avatar/5620cae3d3a6aacd9294167b3883500b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeoSh&#39;s gravatar image" />
<p><span>GeoSh</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeoSh has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 May '12, 17:39</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span></p>
</div>
</div>
<div id="comments-container-11508" class="comments-container">
<span id="11510"></span>
<div id="comment-11510" class="comment">
<div id="post-11510-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please edit your question and tell us:</p>
<p>Do you see any progress indicator that tiles are downloaded at all?</p>
<p>Try to start JTiledownloader from Windows' command prompt like described at <a href="http://wiki.openstreetmap.org/wiki/JTileDownloader">http://wiki.openstreetmap.org/wiki/JTileDownloader</a></p>
<p>As a Java app, maybe you can see any error messges there.</p>
</div>
<div id="comment-11510-info" class="comment-info">
<span class="comment-age">(27 Mar '12, 08:33)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="11531"></span>
<div id="comment-11531" class="comment">
<div id="post-11531-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When JTileDownloader is run directly and "download tiles" clicked, there's no progress indicator or signs of activity. Running program from a command prompt generates a file of which the first few lines are shown below. The rest are mostly more "(Unknown Source")lines.</p>
<p>Exception in thread "AWT-EventQueue-0" java.lang.NoSuchMethodError: java.lang.Integer.compare(II)I at org.openstreetmap.fma.jtiledownloader.datatypes.TileComparatorFactory $QuadComparator.compare(TileComparatorFactory.java:57) at org.openstreetmap.fma.jtiledownloader.datatypes.TileComparatorFactory $QuadComparator.compare(Tile</p>
</div>
<div id="comment-11531-info" class="comment-info">
<span class="comment-age">(27 Mar '12, 15:11)</span> <span class="comment-user userinfo">GeoSh</span>
</div>
</div>
</div>
<div id="comment-tools-11508" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11508-form-container" class="comment-form-container">
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

<span id="11596"></span>

<div id="answer-container-11596" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11596-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11596-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-11596-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="GeoSh has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><strong>Please read the update note below (jTileDownloader 'Backport' to Java SE 5).</strong><br />
Some developer of the jTileDownloader decided it would be a good idea to use the latest and greatest features of Java SE 7 (aka Java v1.7.x) ignoring the fact that almost all people have Java SE 5 (aka v1.5.<em>) or 6 (aka v1.6.</em>) installed...and maybe don't want to upgrade to a newer version for whatever reason (maybe not yet available on the platform of the user).</p>
<p>The Integer.compare(x,y) is one of the new methods introduced in Java SE 7 (aka v1.7.x). See here: <a href="http://docs.oracle.com/javase/7/docs/api/java/lang/Integer.html#compare%28int,%20int%29" title="Java Platform SE 7 - Integer.compare(int, int) - Oracle JavaDoc"></a><a href="http://docs.oracle.com/javase/7/docs/api/java/lang/Integer.html#compare%28int,%20int%29">http://docs.oracle.com/javase/7/docs/api/java/lang/Integer.html#compare%28int,%20int%29</a></p>
<p>This can be fixed easily (changed back to the old behaviour) in about 10 minutes (the link above already shows one working option), so the application would again work with Java 6 (1.6.x). I actually backported it myself a few weeks ago when I downloaded the code and Eclipse showed me some errors, because the selected runtime for the project was Java 1.5 or 1.6. My build is currently not available anywhere and I don't have the time right now to put it on my website. The other solution would be to install Java 7 (1.7.x) which is currently required.</p>
<p>One other thing which not everyone knows. The 64-bit Java Runtime uses round about 1.5 x more memory than the 32-bit Java Runtime and the 64-bit version is normally not faster. Having said that I suggest to install the 32-bit version even on a 64-bit system. There might be a reason to use the 64-bit version on the 64-bit operating system but normally it's not required.</p>
<p><strong><u>Update 1 - 2012-03-31</u></strong><br />
I'm just downloading the source code again to re-apply the fix for the problem (backport to older Java versions). I don't know when I can upload the new 0.6 release to my website...hopefully this weekend.</p>
<p><strong><u>Update 2 - 2012-03-31</u></strong><br />
I've completed the backport. I did only very limited testing but it should work now with Java SE 5 (aka 1.5.x) and Java SE 6 (aka v1.6.x). The applied modification can be found in the package 'org.openstreetmap.fma.jtiledownloader.datatypes'. The class is 'TileComparatorFactory' and the methods changed are 'SimpleComparator.compare(Tile, Tile)' and 'QuadComparator.compare(Tile, Tile)'. Both are inner classes with a compare method.<br />
<a href="http://www.juergen-ulbts.de/content/download/project/ports/jTileDownloader-0-6-0_Java5_2012-03-31.zip" title="jTileDownloader &#39;Backport&#39; for Java SE 5 - Application (2012-03-31)">jTileDownloader v0.6.0 'Backport' for Java SE 5 - Application (2012-03-31)</a><br />
<a href="http://www.juergen-ulbts.de/content/download/project/ports/jTileDownloader-src-0-6-0_Java5_2012-03-31.zip" title="jTileDownloader &#39;Backport&#39; for Java SE 5 - Java Source (2012-03-31)">jTileDownloader v0.6.0 'Backport' for Java SE 5 - Java Source (2012-03-31)</a></p>
<p>A success report would be nice. Thank you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Mar '12, 15:35</strong></p>
<img src="https://secure.gravatar.com/avatar/bc4dda848634a8d38aee40e01a536d8a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="magog001&#39;s gravatar image" />
<p><span>magog001</span><br />
<span class="score" title="96 reputation points">96</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="magog001 has one accepted answer">100%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Mar '12, 13:16</strong> </span></p>
</div>
</div>
<div id="comments-container-11596" class="comments-container">
<span id="11621"></span>
<div id="comment-11621" class="comment">
<div id="post-11621-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks very much for taking the time to address my question. While I consider myself reasonably tech-savvy, when it comes to code-related issues I'm much slower. I understand from your reply that my problem is or might be related to some new technique used in Java SE 7. I see on the java website that 7 is still basically in beta, and not generally available. Unfortunately, looking at the site your link takes me to leaves me clueless about what I'd do with that info. If the above is correct, then I'll just wait for SE 7 to be released, as I'm in no particular hurry to make the downloads work. If I'm misinterpreting your response, please let em know. Thanks again.</p>
</div>
<div id="comment-11621-info" class="comment-info">
<span class="comment-age">(30 Mar '12, 00:33)</span> <span class="comment-user userinfo">GeoSh</span>
</div>
</div>
<span id="11654"></span>
<div id="comment-11654" class="comment">
<div id="post-11654-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The provided link (showing the new function) was more for (Java) developers and not for the end users. Java SE 7 (v1.7.x) has been released at least for Windows in October 2011 by Oracle. Here the Java Downloads offerings by Oracle: <a href="http://www.oracle.com/technetwork/java/javase/downloads/index.html">http://www.oracle.com/technetwork/java/javase/downloads/index.html</a></p>
<p>End-User --&gt; Grab the Java Runtime Environment (JRE)</p>
<p>Developer --&gt; Grab the Java Development Kit (JDK)...it also includes the JRE</p>
<p>Maybe Apple hasn't released a 'final' MacOS X release yet. If that's the case it confirms my rant above that it's a bad idea to use the latest features right away.</p>
</div>
<div id="comment-11654-info" class="comment-info">
<span class="comment-age">(30 Mar '12, 23:59)</span> <span class="comment-user userinfo">magog001</span>
</div>
</div>
<span id="11657"></span>
<div id="comment-11657" class="comment">
<div id="post-11657-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I added download links in my original post to my website where I placed the backport for older Java versions. Some feedback if it works or not would be nice. Thank you!</p>
</div>
<div id="comment-11657-info" class="comment-info">
<span class="comment-age">(31 Mar '12, 13:20)</span> <span class="comment-user userinfo">magog001</span>
</div>
</div>
<span id="12564"></span>
<div id="comment-12564" class="comment">
<div id="post-12564-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I thought I'd get an email anytime something new on this thread showed up, but it didn't for your followups. Very sorry for not having responded, as I just decided to take a peek into the subject today.</p>
<p>Yesterday I did install the (beta?) version of JRE 7 from Oracle and ran the jtiledownloader again, with results identical to before - no tiles. I will next try your application backport on a computer with JRE 6 and let you know the results.</p>
<p>Again, apologies for not getting back to you, and many thanks for your help.</p>
</div>
<div id="comment-12564-info" class="comment-info">
<span class="comment-age">(05 May '12, 17:51)</span> <span class="comment-user userinfo">GeoSh</span>
</div>
</div>
<span id="12587"></span>
<div id="comment-12587" class="comment">
<div id="post-12587-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No problem. With the JRE 7 from Oracle it should work with the original release. Maybe the 'old' JRE is still active? What do you get when you open a command line and run (java needs to be on the PATH to be found): java -version or java -fullversion</p>
</div>
<div id="comment-12587-info" class="comment-info">
<span class="comment-age">(07 May '12, 09:44)</span> <span class="comment-user userinfo">magog001</span>
</div>
</div>
<span id="12593"></span>
<div id="comment-12593" class="comment not_top_scorer">
<div id="post-12593-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I haven't tried running it on a command line, but I did check Java in the control panel of that other computer which indicated version 7. In the meantime your tweaked jtiledownloader ran apparently correctly on this computer with JRE 6, as the folders and png files finally got created as expected. Thanks!</p>
<p>Now I'm on to the next problem with the MapTool not working properly on my Palm Pixi, but hoping to get some guidance from the developers. (Just FYI, installed the tiles in the correct folder in the phone, but MapTool app seems to pull in coordinates for Berlin, not NJ where I am.)</p>
</div>
<div id="comment-12593-info" class="comment-info">
<span class="comment-age">(07 May '12, 14:28)</span> <span class="comment-user userinfo">GeoSh</span>
</div>
</div>
<span id="12596"></span>
<div id="comment-12596" class="comment not_top_scorer">
<div id="post-12596-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>We are going off-topic now but... I've got the Pre2 and Pre3 here and I'm also a Mapping Tool user. Just downloaded the v3.9.0 this afternoon. I assume that Henk Jonas uses the Berlin coordinates (he lives there) as default when the Pixi wasn't able to get the current location yet. What is shown when you switch to "Dash2" (click)? There should be entries (coordinates) for "Start" and "Now". On "Dash1" you can scroll down to get a list of satellites currently used (they written "bold").</p>
</div>
<div id="comment-12596-info" class="comment-info">
<span class="comment-age">(07 May '12, 16:08)</span> <span class="comment-user userinfo">magog001</span>
</div>
</div>
<span id="12597"></span>
<div id="comment-12597" class="comment not_top_scorer">
<div id="post-12597-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Should we take this off-line, or comment further here? I probably need to get an updated version, as I have no idea of what the "Dash..." is.</p>
</div>
<div id="comment-12597-info" class="comment-info">
<span class="comment-age">(07 May '12, 16:28)</span> <span class="comment-user userinfo">GeoSh</span>
</div>
</div>
<span id="12602"></span>
<div id="comment-12602" class="comment not_top_scorer">
<div id="post-12602-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes we should move the Mapping Tool issue to a personal email level. As it seems there is no option here for PM just go to my website (see link above...and remove the stuff pointing to my JTileDownloader build) and once the page is loaded click on contact where an image with an email address shows up. Once I get something from you I'll reply with my real address. The "dash" stuff is also available in older versions (swipe to the left in the left area of the gesture area below the screen...each time you do that something should change...1st the buttons on the map, then the map disappears and the first dash shows up...). The rest via personal email. cu</p>
</div>
<div id="comment-12602-info" class="comment-info">
<span class="comment-age">(08 May '12, 00:57)</span> <span class="comment-user userinfo">magog001</span>
</div>
</div>
</div>
<div id="comment-tools-11596" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-11596-form-container" class="comment-form-container">
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

