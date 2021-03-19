+++
type = "question"
title = "build Wireshark failed"
description = '''Hi, i managed to compile wireshark on windows 8 and now when i try to build it with msbuild /m /p:Configuration=RelWithDebInfo Wireshark.sln command and i get the following message: Build FAILED.  &quot;C:&#92;wireshark-2.0.5&#92;wsbuild64&#92;Wireshark.sln&quot; (default target) (1) -&amp;gt;  &quot;C:&#92;wireshark-2.0.5&#92;wsbuild64&#92;...'''
date = "2016-08-24T06:46:00Z"
lastmod = "2016-08-25T06:34:00Z"
weight = 55094
keywords = [ "build_error", "build" ]
aliases = [ "/questions/55094" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [build Wireshark failed](/questions/55094/build-wireshark-failed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55094-score" class="post-score" title="current number of votes">0</div><span id="post-55094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>i managed to compile wireshark on windows 8 and now when i try to build it with msbuild /m /p:Configuration=RelWithDebInfo Wireshark.sln command and i get the following message:</p><p>Build FAILED.</p><pre><code>   &quot;C:\wireshark-2.0.5\wsbuild64\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;C:\wireshark-2.0.5\wsbuild64\docbook\developer_guide_chm.vcxproj.metapr
   oj&quot; (default target) (14) -&gt;
   &quot;C:\wireshark-2.0.5\wsbuild64\docbook\developer_guide_chm.vcxproj&quot; (defa
   ult target) (83) -&gt;
   (CustomBuild target) -&gt;
     CUSTOMBUILD : warning : failed to load external entity &quot;http://docbook
   .sourceforge.net/release/xsl/current/htmlhelp/htmlhelp.xsl&quot; [C:\wireshar
   k-2.0.5\wsbuild64\docbook\developer_guide_chm.vcxproj]

   &quot;C:\wireshark-2.0.5\wsbuild64\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;C:\wireshark-2.0.5\wsbuild64\docbook\user_guide_chm.vcxproj.metaproj&quot; (
   default target) (53) -&gt;
   &quot;C:\wireshark-2.0.5\wsbuild64\docbook\user_guide_chm.vcxproj&quot; (default t
   arget) (103) -&gt;
     CUSTOMBUILD : warning : failed to load external entity &quot;http://docbook
   .sourceforge.net/release/xsl/current/htmlhelp/htmlhelp.xsl&quot; [C:\wireshar
   k-2.0.5\wsbuild64\docbook\user_guide_chm.vcxproj]

   &quot;C:\wireshark-2.0.5\wsbuild64\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;C:\wireshark-2.0.5\wsbuild64\docbook\developer_guide_chm.vcxproj.metapr
   oj&quot; (default target) (14) -&gt;
   &quot;C:\wireshark-2.0.5\wsbuild64\docbook\developer_guide_chm.vcxproj&quot; (defa
   ult target) (83) -&gt;
   (CustomBuild target) -&gt;
     CUSTOMBUILD : I/O error : Attempt to load network entity http://docboo
   k.sourceforge.net/release/xsl/current/htmlhelp/htmlhelp.xsl [C:\wireshar
   k-2.0.5\wsbuild64\docbook\developer_guide_chm.vcxproj]
     CUSTOMBUILD : compilation error : file /wireshark-2.0.5/docbook/custom
   _layer_chm.xsl line 8 element import [C:\wireshark-2.0.5\wsbuild64\docbo
   ok\developer_guide_chm.vcxproj]

   &quot;C:\wireshark-2.0.5\wsbuild64\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;C:\wireshark-2.0.5\wsbuild64\docbook\user_guide_chm.vcxproj.metaproj&quot; (
   default target) (53) -&gt;
   &quot;C:\wireshark-2.0.5\wsbuild64\docbook\user_guide_chm.vcxproj&quot; (default t
   arget) (103) -&gt;
     CUSTOMBUILD : I/O error : Attempt to load network entity http://docboo
   k.sourceforge.net/release/xsl/current/htmlhelp/htmlhelp.xsl [C:\wireshar
   k-2.0.5\wsbuild64\docbook\user_guide_chm.vcxproj]
     CUSTOMBUILD : compilation error : file /wireshark-2.0.5/docbook/custom
   _layer_chm.xsl line 8 element import [C:\wireshark-2.0.5\wsbuild64\docbo
   ok\user_guide_chm.vcxproj]

2 Warning(s)
4 Error(s)</code></pre><p>i am running the Visual Studio Command Prompt as administrator.</p><p>thanks in advance, Ran</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-build_error" rel="tag" title="see questions tagged &#39;build_error&#39;">build_error</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Aug '16, 06:46</strong></p><img src="https://secure.gravatar.com/avatar/2a790061b6d1f5ec0fb06a4ab6a5e52f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ran&#39;s gravatar image" /><p><span>Ran</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ran has no accepted answers">0%</span></p></div></div><div id="comments-container-55094" class="comments-container"></div><div id="comment-tools-55094" class="comment-tools"></div><div class="clear"></div><div id="comment-55094-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55095"></span>

<div id="answer-container-55095" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55095-score" class="post-score" title="current number of votes">0</div><span id="post-55095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The build is attempting to retrieve an external file:</p><pre><code>CUSTOMBUILD : I/O error : Attempt to load network entity http://docbook.sourceforge.net/release/xsl/current/htmlhelp/htmlhelp.xsl</code></pre><p>Can you manually download that on the same build machine? Is this related to your other issue of not being able to clone the git repo? Does the build machine have internet access or is it behind some form of proxy?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '16, 07:15</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-55095" class="comments-container"><span id="55105"></span><div id="comment-55105" class="comment"><div id="post-55105-score" class="comment-score"></div><div class="comment-text"><p>i can download this file with a browser. the machine have internet access, this is a company's computer so i don't know if it is behind proxy. it is possible that this machine is behind proxy and this is why i could not get the git and the file.</p><p>i looked at the files looking for where to change the address from remote to local ( i downloaded the file from the net and want the project to build with the local file and not the remote one ) but i could not find it.</p></div><div id="comment-55105-info" class="comment-info"><span class="comment-age">(24 Aug '16, 23:10)</span> <span class="comment-user userinfo">Ran</span></div></div><span id="55109"></span><div id="comment-55109" class="comment"><div id="post-55109-score" class="comment-score"></div><div class="comment-text"><p>I've never seen that error reported before, I wonder if it's anything to do with building from a source tarball?</p><p>I don't have the file in either my source or build trees, and there are multiple copies in my Cygwin installation:</p><pre><code>DirectoryName                                                    Length
-------------                                                    ------
C:\Cygwin\etc\asciidoc\docbook-xsl                                  770
C:\Cygwin\usr\share\sgml\docbook\xsl-stylesheets\htmlhelp           924
C:\Cygwin\usr\share\sgml\docbook\xsl-stylesheets\slides\htmlhelp   3182</code></pre></div><div id="comment-55109-info" class="comment-info"><span class="comment-age">(25 Aug '16, 03:18)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="55112"></span><div id="comment-55112" class="comment"><div id="post-55112-score" class="comment-score"></div><div class="comment-text"><p>i connected the computer to the internet and cloned the git and build it. now it took 11:33 minutes (before it took 20 seconds top) to run and at the end i got:</p><p>"C:\Development\wireshark\wsbuild64\Wireshark.sln" (default target) (1) -&gt; "C:\Development\wireshark\wsbuild64\docbook\developer_guide_chm.vcxproj. metaproj" (default target) (15) -&gt; "C:\Development\wireshark\wsbuild64\docbook\developer_guide_chm.vcxproj" (default target) (115) -&gt; (CustomBuild target) -&gt; CUSTOMBUILD : I/O error : Attempt to load network entity <a href="http://docboo">http://docboo</a> k.sourceforge.net/release/xsl/current/htmlhelp/htmlhelp.xsl [C:\Developm ent\wireshark\wsbuild64\docbook\developer_guide_chm.vcxproj] CUSTOMBUILD : compilation error : file /Development/wireshark/docbook/ custom_layer_chm.xsl line 8 element import [C:\Development\wireshark\wsb uild64\docbook\developer_guide_chm.vcxproj]</p><p>"C:\Development\wireshark\wsbuild64\Wireshark.sln" (default target) (1) -&gt; "C:\Development\wireshark\wsbuild64\docbook\user_guide_chm.vcxproj.metap roj" (default target) (64) -&gt; "C:\Development\wireshark\wsbuild64\docbook\user_guide_chm.vcxproj" (def ault target) (118) -&gt; CUSTOMBUILD : I/O error : Attempt to load network entity <a href="http://docboo">http://docboo</a> k.sourceforge.net/release/xsl/current/htmlhelp/htmlhelp.xsl [C:\Developm ent\wireshark\wsbuild64\docbook\user_guide_chm.vcxproj] CUSTOMBUILD : compilation error : file /Development/wireshark/docbook/ custom_layer_chm.xsl line 8 element import [C:\Development\wireshark\wsb uild64\docbook\user_guide_chm.vcxproj]</p><pre><code>85 Warning(s)
4 Error(s)</code></pre><p>Time Elapsed 00:11:33.01</p><p>same error more warnings. i was connected directly to the internet the whole time.</p><p>do you have any other ideas?</p></div><div id="comment-55112-info" class="comment-info"><span class="comment-age">(25 Aug '16, 04:30)</span> <span class="comment-user userinfo">Ran</span></div></div><span id="55114"></span><div id="comment-55114" class="comment"><div id="post-55114-score" class="comment-score"></div><div class="comment-text"><p>A full build does take some time to complete, so 11 minutes isn't unexpected.</p><p>You're still getting the errors on attempting to retrieve htmlhelp.xsl, I can't think when I last built without being connected to the internet, but I assume other folks do it and it hasn't been reported before. The line in the .xsl file that causes the import has been in the source code for 2 years.</p><p>You could try copying the downloaded version into the source docbook directory and editing docbook\custom_layer_chm.xsl to use an import with a local path:</p><pre><code>&lt;xsl:import href=&quot;htmlhelp.xsl&quot;/&gt;</code></pre><p>I have no idea if that will work.</p></div><div id="comment-55114-info" class="comment-info"><span class="comment-age">(25 Aug '16, 06:34)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-55095" class="comment-tools"></div><div class="clear"></div><div id="comment-55095-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

