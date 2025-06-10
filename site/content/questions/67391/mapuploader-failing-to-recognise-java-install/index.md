+++
type = "question"
title = "Mapuploader failing to recognise Java install."
description = '''Hi I&#x27;ve been in contact with the creator of this program &amp;amp; we&#x27;re both stumped as to the cause. https://www.pinns.co.uk/osm/mapuploader5.html Mapuploader should automatically find Java when it&#x27;s installed. I use Java to run a number of tools including mkgmap, so it is working. Mapuploader&#x27;s own t...'''
date = "2018-12-30T14:38:00Z"
lastmod = "2019-01-07T20:45:00Z"
weight = 67391
keywords = [ "java", "mapuploader", "garmin" ]
aliases = [ "/questions/67391" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Mapuploader failing to recognise Java install.](/questions/67391/mapuploader-failing-to-recognise-java-install)

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
<span id="post-67391-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67391-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67391-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I've been in contact with the creator of this program &amp; we're both stumped as to the cause.</p>
<p><a href="https://www.pinns.co.uk/osm/mapuploader5.html">https://www.pinns.co.uk/osm/mapuploader5.html</a></p>
<p>Mapuploader should automatically find Java when it's installed. I use Java to run a number of tools including mkgmap, so it is working. Mapuploader's own testing batch file returns the latest version.</p>
<p>The paths stored in my PATH system variable: C:\Program Files (x86)\Common Files\Oracle\Java\javapath; C:\ProgramData\Oracle\Java\javapath;</p>
<p>Has anyone else had this problem? Can anyone suggest a solution?</p>
<p>Cheers DaveF</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-mapuploader" rel="tag" title="see questions tagged &#39;mapuploader&#39;">mapuploader</span> <span class="post-tag tag-link-garmin" rel="tag" title="see questions tagged &#39;garmin&#39;">garmin</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Dec '18, 14:38</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Dec '18, 14:53</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-67391" class="comments-container">
<span id="67403"></span>
<div id="comment-67403" class="comment">
<div id="post-67403-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I do not have windows nor mapuploader, but the "javapath" in your path looks strange. Does running <code>java -version</code> from a shell work (returns the java version info)? If not, then your paths are wrong.</p>
</div>
<div id="comment-67403-info" class="comment-info">
<span class="comment-age">(31 Dec '18, 14:55)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="67405"></span>
<div id="comment-67405" class="comment">
<div id="post-67405-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes. Mapuploader's testing batch file runs <code>java -version</code></p>
</div>
<div id="comment-67405-info" class="comment-info">
<span class="comment-age">(31 Dec '18, 15:02)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="67406"></span>
<div id="comment-67406" class="comment">
<div id="post-67406-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>so, if this works, I really think there is something wrong with mapuploader. Did the developer try it with the exact same version of java as you? If not try to run the version the dev uses.</p>
</div>
<div id="comment-67406-info" class="comment-info">
<span class="comment-age">(31 Dec '18, 15:33)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="67417"></span>
<div id="comment-67417" class="comment">
<div id="post-67417-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe the actually error message would be helpful?</p>
</div>
<div id="comment-67417-info" class="comment-info">
<span class="comment-age">(01 Jan '19, 22:20)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="67432"></span>
<div id="comment-67432" class="comment">
<div id="post-67432-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Try to set your environment variables as described in <a href="https://stackoverflow.com/a/26640589/1340631">this answer</a>. As aseerel4c26 already noted your java path looks really strange. However I don't have a Windows installation so I can't compare it with mine.</p>
</div>
<div id="comment-67432-info" class="comment-info">
<span class="comment-age">(03 Jan '19, 08:10)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="67437"></span>
<div id="comment-67437" class="comment not_top_scorer">
<div id="post-67437-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a> No real error message. It's a GUI with a red asterisk next to "Java" (indicating it's not found Java)</p>
<p><a href="https://help.openstreetmap.org/users/158/scai">@scai</a> I'll look into it later, but I don't see how the PATH really makes a difference. The whole point of PATH is it allows a program to be run from any directory without knowing it exact location. Java installed it in that folder. As I said <code>java -version</code> shows it's installed correctly.</p>
</div>
<div id="comment-67437-info" class="comment-info">
<span class="comment-age">(03 Jan '19, 14:02)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="67439"></span>
<div id="comment-67439" class="comment not_top_scorer">
<div id="post-67439-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Then either Mapuploader doesn't use PATH to determine where java is installed or Mapuploader sees a different PATH for some reason.</p>
</div>
<div id="comment-67439-info" class="comment-info">
<span class="comment-age">(03 Jan '19, 14:37)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="67451"></span>
<div id="comment-67451" class="comment not_top_scorer">
<div id="post-67451-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are C:\Program Files (x86)\Common Files\Oracle\Java\javapath and C:\ProgramData\Oracle\Java\javapath directories that actually exist? Typically Oracle will install in dirs that look like C:\Program Files\Java\jre1.8.0_111 so I suspect that the "javapath" bit is really just a placeholder for the real directory.</p>
</div>
<div id="comment-67451-info" class="comment-info">
<span class="comment-age">(04 Jan '19, 08:51)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="67497"></span>
<div id="comment-67497" class="comment not_top_scorer">
<div id="post-67497-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"javapath" is what I see on a Windows 7 laptop that's had various versions of Oracle Java on it. Path starts with:</p>
<pre><code>C:\Program Files (x86)\Common Files\Oracle\Java\javapath;C:\ProgramData\Oracle\Java\javapath;C:\Program Files (x86)\Java\jdk1.7.0_45\bin;C:\Windows\system32;C:\Windows;&lt;other_stuff&gt;</code></pre>
<p>Both "javapath" directories actually exist.</p>
<p>java -version gives:</p>
<pre><code>java version &quot;1.8.0_191&quot;</code></pre>
<p>so I'm guessing that it's a recent change.</p>
<p>Personally I'd suggest OpenJDK over "Oracle Java" these days, but this is what this machine historically has on it.</p>
</div>
<div id="comment-67497-info" class="comment-info">
<span class="comment-age">(07 Jan '19, 20:45)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-67391" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-67391-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

