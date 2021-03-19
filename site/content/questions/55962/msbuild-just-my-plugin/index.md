+++
type = "question"
title = "msbuild just my plugin?"
description = '''Forgive me for I&#x27;m accustom to many years of using &quot;nmkake -f Makefile.nmake&quot; in my source plugin directory to only compile my dissector into a .dll file. I&#x27;m at a complete loss of how I would do that now. If I try to target just the plugins&#92;foo&#92;foo.vcxproj with &quot;msbuild /p:Configuration=RelWithDebI...'''
date = "2016-09-28T09:31:00Z"
lastmod = "2016-09-28T09:36:00Z"
weight = 55962
keywords = [ "windows", "compile", "dissector", "msbuild", "plugin" ]
aliases = [ "/questions/55962" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [msbuild just my plugin?](/questions/55962/msbuild-just-my-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55962-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Forgive me for I'm accustom to many years of using "nmkake -f Makefile.nmake" in my source plugin directory to only compile my dissector into a .dll file. I'm at a complete loss of how I would do that now. If I try to target just the plugins\foo\foo.vcxproj with "msbuild /p:Configuration=RelWithDebInfo plugins\foo\adsb.vcxproj", it seems to want to recompile everything in wireshark.</p><p>I have added my plugin to CMakeListsCustom.txt in the source tree and it makes the correct folders in my build directory when I do a prepare. I have succesfully made a complete wireshark build and now I just need to debug and recompile my dissector only.</p></div><div id="question-tags" class="tags-container tags">windows compile dissector msbuild plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Sep '16, 09:31</strong></p><img src="https://secure.gravatar.com/avatar/b363fb1dfec547bd68fa5e3eae8836a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike_P&#39;s gravatar image" /><p>Mike_P<br />
<span class="score" title="30 reputation points">30</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike_P has no accepted answers">0%</span></p></div></div><div id="comments-container-55962" class="comments-container"></div><div id="comment-tools-55962" class="comment-tools"></div><div class="clear"></div><div id="comment-55962-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55963"></span>

<div id="answer-container-55963" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55963-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Search and ye shall find. Sorry, should have done a better search before asking my question. <a href="https://ask.wireshark.org/questions/51161/how-to-compile-the-dissector-to-a-dll-or-shared-library">https://ask.wireshark.org/questions/51161/how-to-compile-the-dissector-to-a-dll-or-shared-library</a> I assumed that it was taking so long that I was not doing the command correctly. It would seem its just a lot longer than compared to the old nmake method.</p><p>Courtesy of grahamb: <em>Yep, just rebuild the whole solution again and it will all work, assuming you've made the correct changes. If you've created a plugin dissector you can just rebuild your plugin by substituting the path to the plugin project file on the msbuild command line, e.g. msbuild /m /p:Configuration=RelWithDebInfo plugins\myplugin\myplugin.vcxproj You must have previously built Wireshark in the build directory though before compiling the plugin on it's own in this manner. You'll find in practice there's only a little time difference between the "full" build and just building the plugin.</em></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '16, 09:36</strong></p><img src="https://secure.gravatar.com/avatar/b363fb1dfec547bd68fa5e3eae8836a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike_P&#39;s gravatar image" /><p>Mike_P<br />
<span class="score" title="30 reputation points">30</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike_P has no accepted answers">0%</span></p></div></div><div id="comments-container-55963" class="comments-container"></div><div id="comment-tools-55963" class="comment-tools"></div><div class="clear"></div><div id="comment-55963-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

