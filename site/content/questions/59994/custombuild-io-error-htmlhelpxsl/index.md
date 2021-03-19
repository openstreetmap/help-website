+++
type = "question"
title = "CUSTOMBUILD : I/O error: htmlhelp.xsl"
description = '''I had cloned 2.3.0 version using git and wireshark build had worked.  However I deleted the Development directory and re-cloned the repository and now am running into following error:  &quot;C:&#92;Development&#92;wsbuild32&#92;Wireshark.sln&quot; (Rebuild target) (1) -&amp;gt;  &quot;C:&#92;Development&#92;wsbuild32&#92;docbook&#92;user_guide_c...'''
date = "2017-03-10T13:14:00Z"
lastmod = "2017-03-10T13:14:00Z"
weight = 59994
keywords = [ "htmlhelp" ]
aliases = [ "/questions/59994" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [CUSTOMBUILD : I/O error: htmlhelp.xsl](/questions/59994/custombuild-io-error-htmlhelpxsl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59994-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I had cloned 2.3.0 version using git and wireshark build had worked. However I deleted the Development directory and re-cloned the repository and now am running into following error:</p><pre><code>  &quot;C:\Development\wsbuild32\Wireshark.sln&quot; (Rebuild target) (1) -&gt;
  &quot;C:\Development\wsbuild32\docbook\user_guide_chm.vcxproj.metaproj&quot; (Rebu
  ild target) (63) -&gt;
  &quot;C:\Development\wsbuild32\docbook\user_guide_chm.vcxproj&quot; (Rebuild targe
  t) (113) -&gt;
  (CustomBuild target) -&gt;
    CUSTOMBUILD : I/O error : Attempt to load network entity http://docboo
  k.sourceforge.net/release/xsl/current/htmlhelp/htmlhelp.xsl [C:\Developm
  ent\wsbuild32\docbook\user_guide_chm.vcxproj]
    CUSTOMBUILD : compilation error : file /Development/wireshark/docbook/
  custom_layer_chm.xsl line 8 element import [C:\Development\wsbuild32\doc
  book\user_guide_chm.vcxproj]

  &quot;C:\Development\wsbuild32\Wireshark.sln&quot; (Rebuild target) (1) -&gt;
  &quot;C:\Development\wsbuild32\docbook\developer_guide_chm.vcxproj.metaproj&quot;
  (Rebuild target) (15) -&gt;
  &quot;C:\Development\wsbuild32\docbook\developer_guide_chm.vcxproj&quot; (Rebuild
  target) (110) -&gt;
    CUSTOMBUILD : I/O error : Attempt to load network entity http://docboo
  k.sourceforge.net/release/xsl/current/htmlhelp/htmlhelp.xsl [C:\Developm
  ent\wsbuild32\docbook\developer_guide_chm.vcxproj]
    CUSTOMBUILD : compilation error : file /Development/wireshark/docbook/
  custom_layer_chm.xsl line 8 element import [C:\Development\wsbuild32\doc
  book\developer_guide_chm.vcxproj]

  &quot;C:\Development\wsbuild32\Wireshark.sln&quot; (Rebuild target) (1) -&gt;
  &quot;C:\Development\wsbuild32\wireshark.vcxproj.metaproj&quot; (Rebuild target) (
  70) -&gt;
  &quot;C:\Development\wsbuild32\wireshark.vcxproj&quot; (Rebuild target) (153) -&gt;
  (Link target) -&gt;
    LINK : fatal error LNK1181: cannot open input file &#39;run\RelWithDebInfo
  \wireshark.lib&#39; [C:\Development\wsbuild32\wireshark.vcxproj]</code></pre><p>85 Warning(s) 5 Error(s)</p><p>I am connected to internet and can see the file if I check it via browser. I tried by deleting wsbuild32 and the error stays. Any ideas on what I am missing?</p></div><div id="question-tags" class="tags-container tags">htmlhelp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '17, 13:14</strong></p><img src="https://secure.gravatar.com/avatar/f9240775213c2976f22cafb258a453dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanj123&#39;s gravatar image" /><p>Sanj123<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanj123 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Mar '17, 13:33</p></div></div><div id="comments-container-59994" class="comments-container"></div><div id="comment-tools-59994" class="comment-tools"></div><div class="clear"></div><div id="comment-59994-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

