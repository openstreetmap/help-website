+++
type = "question"
title = "How to copy custom configuration files to staging directory for inclusion in installer?"
description = '''I have generated the following nsi script, which gets it done - but is there a way to use an environment variable to the local appdata&#92;wireshark folder for the mate file? Section &quot;Custom Deployed Preferences&quot; SecCustomPrefs ;------------------------------------------- SetShellVarContext current !inc...'''
date = "2016-06-30T22:24:00Z"
lastmod = "2016-07-01T02:33:00Z"
weight = 53758
keywords = [ "configuration", "build" ]
aliases = [ "/questions/53758" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to copy custom configuration files to staging directory for inclusion in installer?](/questions/53758/how-to-copy-custom-configuration-files-to-staging-directory-for-inclusion-in-installer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53758-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have generated the following nsi script, which gets it done - but is there a way to use an environment variable to the local appdata\wireshark folder for the mate file?</p><pre><code>Section &quot;Custom Deployed Preferences&quot; SecCustomPrefs
;-------------------------------------------
SetShellVarContext current
!include &quot;VPatchLib.nsh&quot;
SetOutPath &#39;$INSTDIR&#39;
File &quot;${STAGING_DIR}\quantel.mate&quot;
File &quot;${STAGING_DIR}\preferences&quot;
IfFileExists $APPDATA\Wireshark\decode_as_entries 0 patchdecode
; Extract the old file under name &#39;updatefile.txt&#39;
;File /oname=decode_as_entries decode_as_entries_old
; Update the file - it will be replaced with the new version
DetailPrint &quot;Updating decode_as_entries using patch...&quot;
!insertmacro VPatchFile &quot;${STAGING_DIR}\decode_as.pat&quot; &quot;$APPDATA\Wireshark\decode_as_entries&quot; &quot;$APPDATA\Wireshark\temporaryfile.txt&quot;
goto enddecode
patchdecode:
SetOutPath &#39;$APPDATA\Wireshark&#39;
File &quot;${STAGING_DIR}\decode_as_entries&quot;
enddecode:
SetShellVarContext all
SectionEnd</code></pre><p>*Edit - vastly better - dumped the quentin.mate file, and a stub properties file (with some prefdefined filters) into the application directory, so Wireshark loads those first. I've got a small patch that will be applied to decode_as_entries if it exists, otherwise it gets replaced. What would be the recommended way to get the files into the staging directory for deployment, or is it better to keep this as a manual process? Thanks for your help,</p></div><div id="question-tags" class="tags-container tags">configuration build</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '16, 22:24</strong></p><img src="https://secure.gravatar.com/avatar/c4a59238ef906285e110fa429a9a94b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Scott%20Harman&#39;s gravatar image" /><p>Scott Harman<br />
<span class="score" title="46 reputation points">46</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Scott Harman has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Jul '16, 02:34</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-53758" class="comments-container"><span id="53761"></span><div id="comment-53761" class="comment"><div id="post-53761-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-53761-info" class="comment-info"><span class="comment-age">(01 Jul '16, 01:26)</span> Jaap ♦</div></div><span id="53763"></span><div id="comment-53763" class="comment"><div id="post-53763-score" class="comment-score"></div><div class="comment-text"><p>Note I changed the title to better reflect what this question is actually asking.</p></div><div id="comment-53763-info" class="comment-info"><span class="comment-age">(01 Jul '16, 02:34)</span> grahamb ♦</div></div></div><div id="comment-tools-53758" class="comment-tools"></div><div class="clear"></div><div id="comment-53758-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53762"></span>

<div id="answer-container-53762" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53762-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Add a CMakeListsCustom.txt that adds a custom target with a copy command to copy your files from the source location to the staging dir. There's lots of examples of that in the top level CMakeLists.txt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '16, 02:33</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-53762" class="comments-container"><span id="53870"></span><div id="comment-53870" class="comment"><div id="post-53870-score" class="comment-score"></div><div class="comment-text"><p>Hi @grahamb - can you give me a pointer on this please - I'm trying to add either a block or a command, and both are failing - Here's an example of what I've most recently tried which causes a crash:</p><pre><code>#COMMAND (if not exist \&quot;${DATAFILE_DIR}\\quantel.mate\&quot; xcopy     &quot;${CMAKE_SOURCE_DIR}/quantel.mate&quot; &quot;${DATAFILE_DIR}&quot; /D /Y)
#COMMAND (xcopy &quot;${CMAKE_SOURCE_DIR}/preferences&quot; &quot;${DATAFILE_DIR}&quot; /D     /Y)</code></pre></div><div id="comment-53870-info" class="comment-info"><span class="comment-age">(06 Jul '16, 20:06)</span> Scott Harman</div></div><span id="53900"></span><div id="comment-53900" class="comment"><div id="post-53900-score" class="comment-score"></div><div class="comment-text"><p>Something like:</p><pre><code>ADD_CUSTOM_TARGET(copy-quantel-files
    COMMAND  ${CMAKE_COMMAND} -E copy_if_different
        &quot;${CMAKE_SOURCE_DIR}/quantel.mate&quot;
        $&lt;TARGET_FILE_DIR:wireshark&gt;
)</code></pre><p>Although some of those variable definitions might not be set up when your custom file is included.</p></div><div id="comment-53900-info" class="comment-info"><span class="comment-age">(07 Jul '16, 04:58)</span> grahamb ♦</div></div><span id="54176"></span><div id="comment-54176" class="comment"><div id="post-54176-score" class="comment-score"></div><div class="comment-text"><p>Here's the values I've added to CMakeListsCustom.txt The necessary bit was ADD_DEPENDENCIES</p><pre><code>ADD_CUSTOM_TARGET(copy-quantel-files ALL
    COMMAND  ${CMAKE_COMMAND} -E copy_if_different
        &quot;${CMAKE_SOURCE_DIR}/quantel.mate&quot;
        $&lt;TARGET_FILE_DIR:wireshark&gt;
)
ADD_DEPENDENCIES(copy-quantel-files wireshark)</code></pre><p>I've got a bunch of patches and stock preferences in there for first run up.</p></div><div id="comment-54176-info" class="comment-info"><span class="comment-age">(19 Jul '16, 21:54)</span> Scott Harman</div></div></div><div id="comment-tools-53762" class="comment-tools"></div><div class="clear"></div><div id="comment-53762-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

