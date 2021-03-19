+++
type = "question"
title = "Add basic dissector :cmake for .dll error"
description = '''Hi,i try to create my own dissector and i copy all file needed from gryphon plugin dissector and change gryphon name in makefile with my own dissector name but if i use cmake i hade error: this is my cmakeoutput.txt &amp;lt;snipped for=&quot;&quot; brevity=&quot;&quot; as=&quot;&quot; irrelevant=&quot;&quot;&amp;gt;'''
date = "2016-06-06T09:14:00Z"
lastmod = "2016-11-10T05:55:00Z"
weight = 53240
keywords = [ "dissector", "cmake", "dll" ]
aliases = [ "/questions/53240" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Add basic dissector :cmake for .dll error](/questions/53240/add-basic-dissector-cmake-for-dll-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53240-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53240-score" class="post-score" title="current number of votes">0</div><span id="post-53240-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,i try to create my own dissector and i copy all file needed from gryphon plugin dissector and change gryphon name in makefile with my own dissector name but if i use cmake i hade error:</p><p>this is my cmakeoutput.txt</p><p>&lt;snipped for="" brevity="" as="" irrelevant=""&gt;</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-cmake" rel="tag" title="see questions tagged &#39;cmake&#39;">cmake</span> <span class="post-tag tag-link-dll" rel="tag" title="see questions tagged &#39;dll&#39;">dll</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jun '16, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/39c90bff22b6fa58db657d5af50c7899?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kenhero&#39;s gravatar image" /><p><span>kenhero</span><br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kenhero has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Jun '16, 02:03</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-53240" class="comments-container"><span id="53248"></span><div id="comment-53248" class="comment"><div id="post-53248-score" class="comment-score"></div><div class="comment-text"><p>this is my output after debug solution. my dissector is pvs</p><pre><code>Microsoft (R) Build Engine versione 12.0.31101.0
[Microsoft .NET Framework versione 4.0.30319.42000]
Copyright (C) Microsoft Corporation. Tutti i diritti riservati.

&lt;SNIPPED for brevity as irrelevant &gt;

Compilazione NON RIUSCITA.

&quot;C:\development2\wsbuild64\Wireshark.sln&quot; (destinazione predefinita) (1) -&gt;
&quot;C:\development2\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (destinazione predefinita) (2) -&gt;
&quot;C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj.metaproj&quot; (destinazione predefinita) (110) -&gt;
&quot;C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj&quot; (destinazione predefinita) (111) -&gt;
(destinazione: ClCompile) -&gt;
  c:\development2\wireshark\epan\proto.h(863): warning C4228: nonstandard extension used : qualifiers after comma in declarator list are ignored [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(905): warning C4228: nonstandard extension used : qualifiers after comma in declarator list are ignored [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]

&quot;C:\development2\wsbuild64\Wireshark.sln&quot; (destinazione predefinita) (1) -&gt;
&quot;C:\development2\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (destinazione predefinita) (2) -&gt;
&quot;C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj.metaproj&quot; (destinazione predefinita) (110) -&gt;
&quot;C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj&quot; (destinazione predefinita) (111) -&gt;
(destinazione: ClCompile) -&gt;
  c:\development2\wireshark\epan\proto.h(123): error C2054: expected &#39;(&#39; to follow &#39;WS_NORETURN&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(123): error C2085: &#39;proto_report_dissector_bug&#39; : not in formal parameter list [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(505): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(506): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(507): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(508): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(509): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(510): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(511): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(519): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(522): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(523): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(524): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(525): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(528): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(531): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(532): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(533): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(535): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(535): error C2085: &#39;field_display_e&#39; : not in formal parameter list [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(559): error C2085: &#39;hf_ref_type&#39; : not in formal parameter list [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(562): error C2085: &#39;header_field_info&#39; : not in formal parameter list [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(581): error C2061: syntax error : identifier &#39;hf_ref_type&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(583): error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(584): error C2059: syntax error : &#39;}&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(603): error C2061: syntax error : identifier &#39;header_field_info&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(604): error C2059: syntax error : &#39;}&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(617): error C2016: C requires that a struct or union has at least one member [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(617): error C2061: syntax error : identifier &#39;header_field_info&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(627): error C2059: syntax error : &#39;}&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(705): error C2061: syntax error : identifier &#39;field_info&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(707): error C2059: syntax error : &#39;}&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(710): error C2061: syntax error : identifier &#39;proto_tree&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(710): error C2059: syntax error : &#39;;&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(712): error C2061: syntax error : identifier &#39;proto_item&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(712): error C2059: syntax error : &#39;;&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(805): error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(805): error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(805): error C2059: syntax error : &#39;,&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(805): error C2059: syntax error : &#39;)&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(806): error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(806): error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(806): error C2059: syntax error : &#39;,&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(806): error C2059: syntax error : &#39;)&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(808): error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(808): error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(809): error C2146: syntax error : missing &#39;;&#39; before identifier &#39;func&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(809): error C2059: syntax error : &#39;type&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(809): error C2059: syntax error : &#39;)&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(811): error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(811): error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(812): error C2146: syntax error : missing &#39;;&#39; before identifier &#39;func&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(812): error C2059: syntax error : &#39;type&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(812): error C2059: syntax error : &#39;)&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(857): error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(857): error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(857): error C2059: syntax error : &#39;type&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(857): error C2059: syntax error : &#39;)&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(863): error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(863): error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(863): error C2370: &#39;gint&#39; : redefinition; different storage class [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(863): error C2146: syntax error : missing &#39;;&#39; before identifier &#39;idx&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(863): error C2059: syntax error : &#39;)&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(868): error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(868): error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(868): error C2059: syntax error : &#39;)&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(873): error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(873): error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(873): error C2059: syntax error : &#39;)&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(879): error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(879): error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(879): error C2059: syntax error : &#39;type&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(879): error C2059: syntax error : &#39;)&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(885): error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(885): error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(885): error C2059: syntax error : &#39;type&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(885): error C2059: syntax error : &#39;)&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(892): error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(892): error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(892): error C2059: syntax error : &#39;type&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(892): error C2059: syntax error : &#39;)&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(899): error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(899): error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(899): error C2059: syntax error : &#39;type&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(899): error C2059: syntax error : &#39;)&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(905): error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(905): error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(905): error C2370: &#39;gint&#39; : redefinition; different storage class [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(905): error C2146: syntax error : missing &#39;;&#39; before identifier &#39;length&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(905): error C2059: syntax error : &#39;)&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(917): error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(917): error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(917): error C2371: &#39;tvbuff_t&#39; : redefinition; different basic types [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(917): error C2143: syntax error : missing &#39;;&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(917): error C2370: &#39;gint&#39; : redefinition; different storage class [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(917): error C2146: syntax error : missing &#39;;&#39; before identifier &#39;end&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(917): error C2059: syntax error : &#39;)&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(923): error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(923): error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(923): error C2059: syntax error : &#39;)&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(929): error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(929): fatal error C1003: error count exceeds 100; stopping compilation [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]

    Avvisi: 2
    Errori: 102

Tempo trascorso 00:00:21.47</code></pre></div><div id="comment-53248-info" class="comment-info"><span class="comment-age">(06 Jun '16, 11:36)</span> <span class="comment-user userinfo">kenhero</span></div></div></div><div id="comment-tools-53240" class="comment-tools"></div><div class="clear"></div><div id="comment-53240-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53251"></span>

<div id="answer-container-53251" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53251-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53251-score" class="post-score" title="current number of votes">1</div><span id="post-53251-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thank you for your voluminous output, usually I have to ask for more, not in this case.</p><p>Things start going wrong around here:</p><pre><code>&quot;C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj.metaproj&quot; (destinazione predefinita) (110) -&gt;
&quot;C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj&quot; (destinazione predefinita) (111) -&gt;
(destinazione: ClCompile) -&gt;
  c:\development2\wireshark\epan\proto.h(863): warning C4228: nonstandard extension used : qualifiers after comma in declarator list are ignored [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(905): warning C4228: nonstandard extension used : qualifiers after comma in declarator list are ignored [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]

&quot;C:\development2\wsbuild64\Wireshark.sln&quot; (destinazione predefinita) (1) -&gt;
&quot;C:\development2\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (destinazione predefinita) (2) -&gt;
&quot;C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj.metaproj&quot; (destinazione predefinita) (110) -&gt;
&quot;C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj&quot; (destinazione predefinita) (111) -&gt;
(destinazione: ClCompile) -&gt;
  c:\development2\wireshark\epan\proto.h(123): error C2054: expected &#39;(&#39; to follow &#39;WS_NORETURN&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(123): error C2085: &#39;proto_report_dissector_bug&#39; : not in formal parameter list [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(505): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(506): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(507): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(508): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(509): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(510): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(511): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  c:\development2\wireshark\epan\proto.h(519): error C2057: expected constant expression [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]</code></pre><p>The initial warnings in proto.h are odd, and the subsequent errors in proto.h leads me to believe you've defined something in your plugin that has broken subsequent compilation.</p><p>What do you have in the plugin code before the #include that brings in proto.h? You might not be including it directly, but via another include, e.g. epan/packet.h.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '16, 12:33</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-53251" class="comments-container"><span id="53255"></span><div id="comment-53255" class="comment"><div id="post-53255-score" class="comment-score"></div><div class="comment-text"><p>Only 1 error now in my build but i think actually the problem is that wireshark guide says to take "gryphon plugin" as reference but i have to understand that gryphon dissector is a udp dissector while my dissector is tcp dissector and there are difference .</p><p>this is where build failed (the last part of build.txt lol file)</p><pre><code>Compilazione NON RIUSCITA.

&quot;C:\development2\wsbuild64\Wireshark.sln&quot; (destinazione predefinita) (1) -&gt;
&quot;C:\development2\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (destinazione predefinita) (2) -&gt;
&quot;C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj.metaproj&quot; (destinazione predefinita) (110) -&gt;
&quot;C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj&quot; (destinazione predefinita) (111) -&gt;
(destinazione: ClCompile) -&gt; 
  C:\development2\wireshark\plugins\pvs\packet-pvs.c(80): warning C4113: &#39;void (__cdecl *)(tvbuff_t *,packet_info *,proto_tree *)&#39; differs in parameter lists from &#39;dissector_t&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  C:\development2\wireshark\plugins\pvs\packet-pvs.c(80): warning C4133: &#39;function&#39; : incompatible types - from &#39;void (__cdecl *)(tvbuff_t *,packet_info *,proto_tree *)&#39; to &#39;dissector_t&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  C:\development2\wireshark\plugins\pvs\packet-pvs.c(81): warning C4013: &#39;dissector_add&#39; undefined; assuming extern returning int [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  C:\development2\wireshark\plugins\pvs\packet-pvs.c(123): warning C4113: &#39;void (__cdecl *)(tvbuff_t *,packet_info *,proto_tree *)&#39; differs in parameter lists from &#39;dissector_t&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  C:\development2\wireshark\plugins\pvs\packet-pvs.c(123): warning C4133: &#39;function&#39; : incompatible types - from &#39;void (__cdecl *)(tvbuff_t *,packet_info *,proto_tree *)&#39; to &#39;dissector_t&#39; [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]
  C:\development2\wireshark\plugins\pvs\packet-pvs.c(138): warning C4013: &#39;check_col&#39; undefined; assuming extern returning int [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]

&quot;C:\development2\wsbuild64\Wireshark.sln&quot; (destinazione predefinita) (1) -&gt;
&quot;C:\development2\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (destinazione predefinita) (2) -&gt;
&quot;C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj.metaproj&quot; (destinazione predefinita) (110) -&gt;
&quot;C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj&quot; (destinazione predefinita) (111) -&gt;
(destinazione: ClCompile) -&gt; 
  C:\development2\wireshark\plugins\pvs\packet-pvs.c(80): error C2220: warning treated as error - no &#39;object&#39; file generated [C:\development2\wsbuild64\plugins\pvs\pvs.vcxproj]</code></pre></div><div id="comment-53255-info" class="comment-info"><span class="comment-age">(06 Jun '16, 15:35)</span> <span class="comment-user userinfo">kenhero</span></div></div><span id="53264"></span><div id="comment-53264" class="comment"><div id="post-53264-score" class="comment-score"></div><div class="comment-text"><p>Your issue is still with the code in your dissector, unless you show it to us, e.g. github or similar, we're just guessing.</p><p>To make the dissector use udp instead of tcp you'll need to modify the <code>dissector_add_uint()</code> call to register with a udp port, and then remove the call to <code>tcp_dissect_pdus()</code> as you're no longer using tcp. Instead, using the gryphon dissector as an example, you should just call <code>return dissect_gryphon_pdu(tvb, pinfo, tree, data);</code></p></div><div id="comment-53264-info" class="comment-info"><span class="comment-age">(07 Jun '16, 02:00)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="53265"></span><div id="comment-53265" class="comment"><div id="post-53265-score" class="comment-score"></div><div class="comment-text"><p>i try to follow this link <a href="http://www.codeproject.com/Articles/19426/Creating-Your-Own-Custom-Wireshark-Dissector">link text</a></p><p>even if i merged this guide with wireshark 9.2 guide because,for example,i can use nmake with last wireshark version to creat a dissector .dll</p></div><div id="comment-53265-info" class="comment-info"><span class="comment-age">(07 Jun '16, 02:08)</span> <span class="comment-user userinfo">kenhero</span></div></div><span id="53268"></span><div id="comment-53268" class="comment"><div id="post-53268-score" class="comment-score"></div><div class="comment-text"><p><span>@kenhero</span></p><p>Yet again I've converted your "answer" to a comment, please read the site FAQ for more info.</p><p>That link is hopelessly out of date, most external articles about wireshark are never updated after they're written while the wireshark project moves on. Use the current <a href="https://www.wireshark.org/docs/wsdg_html_chunked/">Wireshark Developers Guide</a> if you're building with sources from master (or 2.0).</p></div><div id="comment-53268-info" class="comment-info"><span class="comment-age">(07 Jun '16, 02:54)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="53320"></span><div id="comment-53320" class="comment"><div id="post-53320-score" class="comment-score"></div><div class="comment-text"><p>Finally i solved the issue and build without errors. Btw I can't follow the wireshark developer guide completely because,for example, it defines in chapter 9.2.2. Dissecting the details of the protocol: static void dissect_foo(tvbuff_t <em>tvb, packet_info</em> pinfo, proto_tree *tree)</p><p>instead of static int dissect_pvs(tvbuff_t <em>tvb, packet_info</em> pinfo, proto_tree <em>tree, void</em> data)</p></div><div id="comment-53320-info" class="comment-info"><span class="comment-age">(08 Jun '16, 09:06)</span> <span class="comment-user userinfo">kenhero</span></div></div><span id="53325"></span><div id="comment-53325" class="comment not_top_scorer"><div id="post-53325-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the report, I updated the developer's guide to update the sample code: <a href="https://code.wireshark.org/review/#/c/15783">https://code.wireshark.org/review/#/c/15783</a></p></div><div id="comment-53325-info" class="comment-info"><span class="comment-age">(08 Jun '16, 13:29)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="53339"></span><div id="comment-53339" class="comment not_top_scorer"><div id="post-53339-score" class="comment-score"></div><div class="comment-text"><p>Another error: Example 9.8. Wrapping up the packet dissection.</p><p>void proto_tree_add_item(foo_tree, hf_foo_pdu_type, tvb, offset, 1, ENC_BIG_ENDIAN);</p><p>It's now :</p><p>proto_item <em>proto_tree_add_item(proto_tree</em> tree, int hfindex, tvbuff_t *tvb, const gint start, gint length, const guint encoding);</p></div><div id="comment-53339-info" class="comment-info"><span class="comment-age">(09 Jun '16, 08:56)</span> <span class="comment-user userinfo">kenhero</span></div></div><span id="53340"></span><div id="comment-53340" class="comment not_top_scorer"><div id="post-53340-score" class="comment-score"></div><div class="comment-text"><p>I don't see the issue in Example 9.8, the calls that use the returned value assign it to a variable of type <code>proto_item*</code>.</p></div><div id="comment-53340-info" class="comment-info"><span class="comment-age">(09 Jun '16, 09:33)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="53341"></span><div id="comment-53341" class="comment not_top_scorer"><div id="post-53341-score" class="comment-score"></div><div class="comment-text"><p>yes but in the guide proto_tree_add_item returns void</p></div><div id="comment-53341-info" class="comment-info"><span class="comment-age">(09 Jun '16, 12:51)</span> <span class="comment-user userinfo">kenhero</span></div></div><span id="53344"></span><div id="comment-53344" class="comment not_top_scorer"><div id="post-53344-score" class="comment-score"></div><div class="comment-text"><p>I've searched the current Developers Guide asciidoc sources and the <a href="https://www.wireshark.org/docs/wsdg_html/">on-line version</a> and none of the 16 references to <code>proto_tree_add_item</code> show a void return or mention void as a return value.</p><p>Are you looking at the latest version of the Developers guide, and if so can you please show the exact excerpt where you see the problem?</p></div><div id="comment-53344-info" class="comment-info"><span class="comment-age">(10 Jun '16, 02:32)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="57261"></span><div id="comment-57261" class="comment not_top_scorer"><div id="post-57261-score" class="comment-score"></div><div class="comment-text"><p><span>@kenhero</span> I am also having the same Errors, how did you solve the Errors??</p></div><div id="comment-57261-info" class="comment-info"><span class="comment-age">(10 Nov '16, 05:55)</span> <span class="comment-user userinfo">xaheen</span></div></div></div><div id="comment-tools-53251" class="comment-tools"><span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a></div><div class="clear"></div><div id="comment-53251-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

