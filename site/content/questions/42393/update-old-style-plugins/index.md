+++
type = "question"
title = "Update &quot;old style&quot; plugins"
description = '''In the file Readme.Plugins it says: Move relevant code from the blocks and delete these functions:  #ifndef ENABLE_STATIC  plugin_reg_handoff()  ....  #endif   #ifndef ENABLE_STATIC  plugin_register()  ....  #endif  Where would I move my code and what changes do I need to make. I currently have the ...'''
date = "2015-05-14T07:18:00Z"
lastmod = "2015-05-16T11:07:00Z"
weight = 42393
keywords = [ "style", "plugin", "wireshark" ]
aliases = [ "/questions/42393" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Update "old style" plugins](/questions/42393/update-old-style-plugins)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42393-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>In the file Readme.Plugins it says:</p><p>Move relevant code from the blocks and delete these functions:</p><pre><code>    #ifndef ENABLE_STATIC
    plugin_reg_handoff()
    ....
    #endif

    #ifndef ENABLE_STATIC
    plugin_register()
    ....
    #endif</code></pre><p>Where would I move my code and what changes do I need to make. I currently have the following:</p><pre><code>#ifndef ENABLE_STATIC
G_MODULE_EXPORT 
void plugin_register(void)
{
    /* register the new protocol, protocol fields, and subtrees */
    if (proto_arr == -1) 
        { /* execute protocol initialization only once */
            proto_register_arr();
        }
}

G_MODULE_EXPORT 
void plugin_reg_handoff(void)
{
    proto_reg_handoff_arr();
}
#endif</code></pre></div><div id="question-tags" class="tags-container tags">style plugin wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 May '15, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/42f084d62348c04d00bd67b129116cc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="XQW1123&#39;s gravatar image" /><p>XQW1123<br />
<span class="score" title="46 reputation points">46</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="XQW1123 has no accepted answers">0%</span></p></div></div><div id="comments-container-42393" class="comments-container"></div><div id="comment-tools-42393" class="comment-tools"></div><div class="clear"></div><div id="comment-42393-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42441"></span>

<div id="answer-container-42441" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42441-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You have no 'relevant code' in the sense meant by README.plugins. This code can simply be dropped, because it will be properly generated during the build.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '15, 11:07</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-42441" class="comments-container"><span id="42562"></span><div id="comment-42562" class="comment"><div id="post-42562-score" class="comment-score"></div><div class="comment-text"><p>I dropped the code, but now I get an error whenever I start wireshark... "The plugin 'xyz.dll' has no registration routines"</p></div><div id="comment-42562-info" class="comment-info"><span class="comment-age">(19 May '15, 13:50)</span> XQW1123</div></div><span id="42589"></span><div id="comment-42589" class="comment"><div id="post-42589-score" class="comment-score">1</div><div class="comment-text"><p>Clean your build of the plugin, before trying again. This triggers the necessary scripting to generate the required code.</p></div><div id="comment-42589-info" class="comment-info"><span class="comment-age">(20 May '15, 11:23)</span> Jaap ♦</div></div></div><div id="comment-tools-42441" class="comment-tools"></div><div class="clear"></div><div id="comment-42441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

