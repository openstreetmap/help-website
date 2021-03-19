+++
type = "question"
title = "Add new columns in the Preferences"
description = '''Hello, I have added new columns along with default columns like Source,Destination,protocol etc in the epan/prefs.c init_prefs() function but they are not at all being reflected at the runtime.'''
date = "2011-09-05T23:44:00Z"
lastmod = "2011-12-02T11:04:00Z"
weight = 6104
keywords = [ "development", "preferences", "columns" ]
aliases = [ "/questions/6104" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Add new columns in the Preferences](/questions/6104/add-new-columns-in-the-preferences)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6104-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have added new columns along with default columns like Source,Destination,protocol etc in the epan/prefs.c init_prefs() function but they are not at all being reflected at the runtime.</p></div><div id="question-tags" class="tags-container tags">development preferences columns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Sep '11, 23:44</strong></p><img src="https://secure.gravatar.com/avatar/968cc7ddfc48322ffbd1d7f5e3d37b85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terrestrial%20shark&#39;s gravatar image" /><p>Terrestrial ...<br />
<span class="score" title="96 reputation points">96</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terrestrial shark has 3 accepted answers">42%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Sep '11, 16:18</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6104" class="comments-container"><span id="6137"></span><div id="comment-6137" class="comment"><div id="post-6137-score" class="comment-score">1</div><div class="comment-text"><p>Why are you trying to do this? Can't you just add a custom column?</p></div><div id="comment-6137-info" class="comment-info"><span class="comment-age">(06 Sep '11, 13:18)</span> cmaynard ♦♦</div></div><span id="6143"></span><div id="comment-6143" class="comment"><div id="post-6143-score" class="comment-score"></div><div class="comment-text"><p>@Prashanth, To be clear, @cmaynard is referring to the <a href="http://www.wireshark.org/docs/wsug_html/#ChCustPreferencesSection">GUI Preferences</a> (not code).</p><p>From your recent posts, it seems like you're trying to hard-code things that are normally read from the <code>preferences</code> file.</p></div><div id="comment-6143-info" class="comment-info"><span class="comment-age">(06 Sep '11, 16:25)</span> helloworld</div></div><span id="6145"></span><div id="comment-6145" class="comment"><div id="post-6145-score" class="comment-score"></div><div class="comment-text"><p>I guess you are trying to get those preferences even after packaging .... I'm not sure which file would reflect those changes ....</p></div><div id="comment-6145-info" class="comment-info"><span class="comment-age">(06 Sep '11, 21:46)</span> flashkicker</div></div><span id="6146"></span><div id="comment-6146" class="comment"><div id="post-6146-score" class="comment-score"></div><div class="comment-text"><p>@flashkicker Yes you are right. What i want ultimately is just to have an installer with the defaults set by me so that whenever i use wireshark i may need no changes for settings.</p></div><div id="comment-6146-info" class="comment-info"><span class="comment-age">(06 Sep '11, 21:50)</span> Terrestrial ...</div></div></div><div id="comment-tools-6104" class="comment-tools"></div><div class="clear"></div><div id="comment-6104-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7746"></span>

<div id="answer-container-7746" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7746-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I would <strong>strongly</strong> suggest that you do this with a global preferences file. The global preferences file is a file named <code>preferences</code> in Wireshark's "global data directory".</p><p>On Windows, the "global data directory" is the installation directory that contains the Wireshark executable.</p><p>On UN*X:</p><ul><li>If the <code>WIRESHARK_DATA_DIR</code> environment variable is set and Wireshark/TShark isn't running set-UID or set-GID, it's the directory specified by that environment variable. That would be the case for the Mac OS X binary package, where it's in the <code>Contents/Resources/share</code> subdirectory of the top-level application bundle directory.</li><li>If the <code>WIRESHARK_DATA_DIR</code> environment variable is not set (or Wireshark/TShark <em>is</em> running set-UID or set-GID, which it probably shouldn't be!), it's the <code>share/wireshark</code> subdirectory of whatever the "top-level" installation directory is; for example, if Wireshark is installed in <code>/usr/local/bin</code>, the "global data directory" would be <code>/usr/local/share/wireshark</code>, the "top-level" installation directory being <code>/usr/local</code>.</li></ul><p>If you insist on doing it with code changes, note that <code>cfmt-&gt;custom_field</code> is expected to have been allocated by <code>g_malloc()</code>, so you'd have to do <code>cfmt-&gt;custom_field = g_strdup("myprotocol.myfield");</code>. You will, however, probably have fewer difficulties and have to ask fewer questions - and will get more sympathy for your questions - if you do this with a global preferences file.</p><p>No matter whether you do it with a global preferences file or a code change, whatever you do will be overridden by the columns in the user preferences file, so you'd have to remove your preferences file or edit it with a text editor so that it doesn't set the columns (remove the <code>column.format</code> preference setting).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '11, 11:04</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7746" class="comments-container"><span id="7765"></span><div id="comment-7765" class="comment"><div id="post-7765-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot!! Great. Its working well now.</p></div><div id="comment-7765-info" class="comment-info"><span class="comment-age">(04 Dec '11, 23:55)</span> Terrestrial ...</div></div></div><div id="comment-tools-7746" class="comment-tools"></div><div class="clear"></div><div id="comment-7746-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6150"></span>

<div id="answer-container-6150" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6150-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The hardcoded preferences are only used when Wireshark does not find a preferences file. So in order for your changes to take effect, you will need to remove your old preferences file before starting up your version of Wireshark.</p><p>If you want to have the same preferences on different systems, you can also distribute your preferences between the systems. Personally I have made my wireshark profiles directory a link to a directory in my dropbox account so I have all profiles available on all my systems.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '11, 00:15</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6150" class="comments-container"><span id="6172"></span><div id="comment-6172" class="comment"><div id="post-6172-score" class="comment-score"></div><div class="comment-text"><p>where do we find the old preferences file on windows machine?</p></div><div id="comment-6172-info" class="comment-info"><span class="comment-age">(07 Sep '11, 04:12)</span> Terrestrial ...</div></div><span id="6186"></span><div id="comment-6186" class="comment"><div id="post-6186-score" class="comment-score"></div><div class="comment-text"><p>When you open Wireshark and go to "Help -&gt; About Wireshark" you can click on the "Folders" tab and it will show you where the personal and system-wide settings are stored.</p><p>Delete all the files in these directories before starting up your version of Wireshark.</p></div><div id="comment-6186-info" class="comment-info"><span class="comment-age">(07 Sep '11, 07:26)</span> SYN-bit ♦♦</div></div><span id="7737"></span><div id="comment-7737" class="comment"><div id="post-7737-score" class="comment-score"></div><div class="comment-text"><p>I hardcoded custom columns and it is running properly in Windows machine but when it comes to ubuntu it is resulting in "Segmentation Fault" error whenever I click on CANCEL of Preferences Dialog box. My code is:</p><pre><code>static void
init_prefs(void) {</code></pre><p>....</p><pre><code>const gchar *col_fmt[] = { &quot;No.&quot;,      &quot;%m&quot;, &quot;Time&quot;,        &quot;%t&quot;,
                        &quot;Source&quot;,   &quot;%s&quot;, &quot;Destination&quot;, &quot;%d&quot;,
                        &quot;Protocol&quot;, &quot;%p&quot;, &quot;Length&quot;,      &quot;%L&quot;,
                        &quot;Info&quot;,     &quot;%Cus&quot;};</code></pre><p>...</p><pre><code>cfmt-&gt;custom_field = &quot;myprotocol.myfield&quot;;</code></pre><p>... }</p><p>&amp; crashes WS</p></div><div id="comment-7737-info" class="comment-info"><span class="comment-age">(01 Dec '11, 23:33)</span> Terrestrial ...</div></div></div><div id="comment-tools-6150" class="comment-tools"></div><div class="clear"></div><div id="comment-6150-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

