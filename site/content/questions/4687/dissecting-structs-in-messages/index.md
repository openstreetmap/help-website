+++
type = "question"
title = "Dissecting structs in messages."
description = '''Hi I am building a protocol that is dissecting message traffic in our system. Now it&#x27;s a flat solution but as several messages shares structs here and there I try to extract these to standalone dissectors. The problem I receive is that the headers need to be intact for the array_length to work. It d...'''
date = "2011-06-23T00:01:00Z"
lastmod = "2011-06-26T22:26:00Z"
weight = 4687
keywords = [ "header", "error" ]
aliases = [ "/questions/4687" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dissecting structs in messages.](/questions/4687/dissecting-structs-in-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4687-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4687-score" class="post-score" title="current number of votes">0</div><span id="post-4687-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I am building a protocol that is dissecting message traffic in our system. Now it's a flat solution but as several messages shares structs here and there I try to extract these to standalone dissectors. The problem I receive is that the headers need to be intact for the array_length to work. It does not include the subpart.</p><p>This is the default header.</p><pre><code>static hf_register_info hf_af_guictrl_FunctionInformationChange_Ind[] =
{
  {
    &amp;hf_af_guictrl_FuInCh_InFu_Gu11,
    {
      &quot;guifunction&quot;, &quot;guictrl.functioninformationchangeind.functionstate.guifunction&quot;,
      FT_UINT16, BASE_DEC, VALS(GuiCtrlFunction_type_name), 0x0,
      NULL, HFILL
    }
  },
  {
    &amp;hf_af_guictrl_FuInCh_InFu_Ac12,
    {
      &quot;accesslevel&quot;, &quot;guictrl.functioninformationchangeind.functionstate.accesslevel&quot;,
      FT_UINT8, BASE_DEC, VALS(GuiCtrlAccessLevel_type_name), 0x0,
      NULL, HFILL
    }
  },
  {
    &amp;hf_af_guictrl_FuInCh_InFuBu_Co131,
    {
      &quot;button.component&quot;, &quot;guictrl.functioninformationchangeind.functionstate.button.component&quot;,
      FT_UINT32, BASE_DEC, VALS(AFComponentID_type_name), 0x0,
      NULL, HFILL
    }
  },
  {
    &amp;hf_af_guictrl_FuInCh_InFuBu_St132,
    {
      &quot;button.state&quot;, &quot;guictrl.functioninformationchangeind.functionstate.button.state&quot;,
      FT_UINT32, BASE_DEC, VALS(GUICTRL_BUTTON_STATE_type_name), 0x0,
      NULL, HFILL
    }
  },
  {
    &amp;hf_af_guictrl_FuInCh_InFuBu_Co133,
    {
      &quot;button.control&quot;, &quot;guictrl.functioninformationchangeind.functionstate.button.control&quot;,
      FT_UINT32, BASE_DEC, VALS(GUICTRL_BUTTON_CONTROL_STATE_type_name), 0x0,
      NULL, HFILL
    }
  },
  {
    &amp;hf_af_guictrl_FuInCh_InFuTo_Co141,
    {
      &quot;toggle.component&quot;, &quot;guictrl.functioninformationchangeind.functionstate.toggle.component&quot;,
      FT_UINT32, BASE_DEC, VALS(AFComponentID_type_name), 0x0,
      NULL, HFILL
    }
  },
  {
    &amp;hf_af_guictrl_FuInCh_InFuTo_St142,
    {
      &quot;toggle.state&quot;, &quot;guictrl.functioninformationchangeind.functionstate.toggle.state&quot;,
      FT_UINT32, BASE_DEC, VALS(GUICTRL_TOGGLE_STATE_type_name), 0x0,
      NULL, HFILL
    }
  },
  {
    &amp;hf_af_guictrl_FuInCh_InFuTo_Co143,
    {
      &quot;toggle.control&quot;, &quot;guictrl.functioninformationchangeind.functionstate.toggle.control&quot;,
      FT_UINT32, BASE_DEC, VALS(GUICTRL_BUTTON_CONTROL_STATE_type_name), 0x0,
      NULL, HFILL
    }
  },
  {
    &amp;hf_af_guictrl_FuInCh_InFu_Co15,
    {
      &quot;controlledbyfunction&quot;, &quot;guictrl.functioninformationchangeind.functionstate.controlledbyfunction&quot;,
      FT_UINT16, BASE_DEC, VALS(GuiCtrlFunction_type_name), 0x0,
      NULL, HFILL
    }
  },
  {
    &amp;hf_af_guictrl_FuInCh_In_Si2,
    {
      &quot;size&quot;, &quot;guictrl.functioninformationchangeind.size&quot;,
      FT_UINT16, BASE_DEC, NULL, 0x0,
      NULL, HFILL
    }
  },
};</code></pre><p>This is the extracted part:</p><pre><code>static hf_register_info hf_af_guictrl_toggle_struct[]=
{
  {
    &amp;hf_af_guictrl_FuIn_RsFuTo_Co1412,
    {
      &quot;component&quot;, &quot;guictrl.toggle.component&quot;,
      FT_UINT32, BASE_DEC, VALS(AFComponentID_type_name), 0x0,
      NULL, HFILL
    }
  },
  {
    &amp;hf_af_guictrl_FuIn_RsFuTo_St1422,
    {
      &quot;state&quot;, &quot;guictrl.toggle.state&quot;,
      FT_UINT32, BASE_DEC, VALS(GUICTRL_TOGGLE_STATE_type_name), 0x0,
      NULL, HFILL
    }
  },
  {
    &amp;hf_af_guictrl_FuIn_RsFuTo_Co1432,
    {
      &quot;control&quot;, &quot;guictrl.toggle.control&quot;,
      FT_UINT32, BASE_DEC, VALS(GUICTRL_BUTTON_CONTROL_STATE_type_name), 0x0,
      NULL, HFILL
    }
  },
};</code></pre><p>This works for me now, but I have duplicated the header info about the toggle part that is a struct containing of 3 datatypes. If I try to remove these from the hf_af_guictrl_FunctionInformationChange_Ind I get the (guint)hfindex &lt; gpa_hfinfo.len error. I dont want to duplicate the information but it seems to be the only way now as the <code>proto_register_field_array(proto_af_guictrl, hf_af_guictrl_FunctionInformationChange_Ind, array_length(hf_af_guictrl_FunctionInformationChange_Ind));</code> seems to fail otherwise.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-header" rel="tag" title="see questions tagged &#39;header&#39;">header</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '11, 00:01</strong></p><img src="https://secure.gravatar.com/avatar/7fc34a297b319c2e052d7e9f0c5a4b48?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scrier&#39;s gravatar image" /><p><span>scrier</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scrier has no accepted answers">0%</span></p></div></div><div id="comments-container-4687" class="comments-container"></div><div id="comment-tools-4687" class="comment-tools"></div><div class="clear"></div><div id="comment-4687-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4762"></span>

<div id="answer-container-4762" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4762-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4762-score" class="post-score" title="current number of votes">0</div><span id="post-4762-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hmm, tried the following subsetion:</p><pre><code>  {
    &amp;hf_af_guictrl_FuInCh_InFuBu_Co133,
    {
      &quot;button.control&quot;, &quot;guictrl.functioninformationchangeind.functionstate.button.control&quot;,
      FT_UINT32, BASE_DEC, VALS(GUICTRL_BUTTON_CONTROL_STATE_type_name), 0x0,
      NULL, HFILL
    }
  },
  {
    &amp;hf_af_guictrl_toggle_struct,
  },
/*  {
    &amp;hf_af_guictrl_FuInCh_InFuTo_Co141,
    {
      &quot;toggle.component&quot;, &quot;guictrl.functioninformationchangeind.functionstate.toggle.component&quot;,
      FT_UINT32, BASE_DEC, VALS(AFComponentID_type_name), 0x0,
      NULL, HFILL
    }
  },
  {
    &amp;hf_af_guictrl_FuInCh_InFuTo_St142,
    {
      &quot;toggle.state&quot;, &quot;guictrl.functioninformationchangeind.functionstate.toggle.state&quot;,
      FT_UINT32, BASE_DEC, VALS(GUICTRL_TOGGLE_STATE_type_name), 0x0,
      NULL, HFILL
    }
  },
  {
    &amp;hf_af_guictrl_FuInCh_InFuTo_Co143,
    {
      &quot;toggle.control&quot;, &quot;guictrl.functioninformationchangeind.functionstate.toggle.control&quot;,
      FT_UINT32, BASE_DEC, VALS(GUICTRL_BUTTON_CONTROL_STATE_type_name), 0x0,
      NULL, HFILL
    }
  },*/
  {
    &amp;hf_af_guictrl_FuInCh_InFu_Co15,
    {
      &quot;controlledbyfunction&quot;, &quot;guictrl.functioninformationchangeind.functionstate.controlledbyfunction&quot;,
      FT_UINT16, BASE_DEC, VALS(GuiCtrlFunction_type_name), 0x0,
      NULL, HFILL
    }
  },</code></pre><p>Still gives me the "(guint)hfindex &lt; gpa_hfinfo.len" on line 1770 in proto.c How do you declare subsection without adding duplicates of the fields?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '11, 22:26</strong></p><img src="https://secure.gravatar.com/avatar/7fc34a297b319c2e052d7e9f0c5a4b48?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scrier&#39;s gravatar image" /><p><span>scrier</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scrier has no accepted answers">0%</span></p></div></div><div id="comments-container-4762" class="comments-container"></div><div id="comment-tools-4762" class="comment-tools"></div><div class="clear"></div><div id="comment-4762-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

