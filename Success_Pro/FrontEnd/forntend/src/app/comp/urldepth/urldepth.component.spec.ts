import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UrldepthComponent } from './urldepth.component';

describe('UrldepthComponent', () => {
  let component: UrldepthComponent;
  let fixture: ComponentFixture<UrldepthComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UrldepthComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UrldepthComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
